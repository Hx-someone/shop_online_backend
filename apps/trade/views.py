import time
from datetime import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import mixins
from django.shortcuts import redirect

from .serializers import *
from utils.permissions import IsOwnerOrReadOnly
from .models import ShoppingCart, OrderInfo, OrderGoods
from users.models import UserProfile


class ShoppingCartViewset(viewsets.ModelViewSet):
    # 这个也没什么好讲的，permission_classes里面的两个字段是确定每个人的购物车信息只能由自己修改
    """
    购物车功能
    list:
        获取购物车详情
    create：
        加入购物车
    delete：
        删除购物记录
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ShopCartSerializer

    # queryset = ShoppingCart.objects.all()
    lookup_field = "goods_id"

    def perform_create(self, serializer):
        shop_cart = serializer.save()
        goods = shop_cart.goods
        goods.goods_num -= shop_cart.nums
        goods.save()

    def perform_destroy(self, instance):
        goods = instance.goods
        goods.goods_num += instance.nums
        goods.save()
        instance.delete()

    def perform_update(self, serializer):
        existed_record = ShoppingCart.objects.get(id=serializer.instance.id)
        existed_nums = existed_record.nums
        saved_record = serializer.save()
        nums = saved_record.nums-existed_nums
        goods = saved_record.goods
        goods.goods_num += nums
        goods.save()

    def get_serializer_class(self):
        if self.action == 'list':
            return ShopCartDetailSerializer
        else:
            return ShopCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class IntegralgoodsCartViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = IntegralgoodsCartSerializer

    lookup_field = "goods_id"

    def perform_create(self, serializer):
        shop_cart = serializer.save()
        goods = shop_cart.goods
        goods.goods_num -= shop_cart.nums
        goods.save()

    def get_serializer_class(self):
        if self.action == 'list':
            return IntegralgoodsCartDetailSerializer
        else:
            return IntegralgoodsCartSerializer

    def get_queryset(self):
        return IntegralgoodsCart.objects.filter(user=self.request.user)


class OrderViewset(viewsets.ModelViewSet):
    """
        订单管理
        list:
            获取个人订单
        delete:
            删除订单
        create：
            新增订单
        """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return OrderInfo.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        # 以下字段都是不可以写入
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            order_goods.save()
            # 请求完订单之后删除所有的商品
            shop_cart.delete()
        return order


from rest_framework.views import APIView
from utils.alipay import AliPay
from shop_online_backend.settings import ali_pub_key_path, private_key_path
from rest_framework.response import Response
from django.shortcuts import  redirect, HttpResponse
from django.http import HttpResponseRedirect


class AlipayView(APIView):
    def get(self, request):
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid="2016101200666258",
            app_notify_url="http://127.0.0.1:8000/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )

        verify_re = alipay.verify(processed_dict, sign)

        if verify_re is True:
            order_sn = processed_dict.get('out_trade_no', None)
            trade_no = processed_dict.get('trade_no', None)
            total_amount = processed_dict.get('total_amount',None)
            trade_status = processed_dict.get('trade_status','Picking')

            userprofile = UserProfile.objects.filter(username = self.request.user)
            for i in range(len(userprofile)):
                userprofile[i].integral += float(total_amount)
                userprofile[i].save()



            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            for existed_order in existed_orders:
                order_goods = existed_order.goods.all()
                for order_good in order_goods:
                    goods = order_good.goods
                    goods.sold_num += order_good.goods_num
                    goods.save()

                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                # existed_order.total_amount = total_amount
                existed_order.pay_time = datetime.now()
                existed_order.save()

            return HttpResponseRedirect('http://127.0.0.1:8080/userOrder')
        else:
            return HttpResponse('支付失败')

    def post(self, request):
        processed_dict = {}
        for key, value in request.POST.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)


        alipay = AliPay(
            appid="2016101200666258",
            app_notify_url="http://127.0.0.1:8000/alipay/return/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )

        verify_re = alipay.verify(processed_dict, sign)

        if verify_re is True:
            order_sn = processed_dict.get('out_trade_no', None)  # 商户网站唯一订单号
            trade_no = processed_dict.get('trade_no', None)  # 支付宝交易流水号
            # total_amount = processed_dict.get('total_amount',None)    #交易的总额
            trade_status = processed_dict.get('trade_status', 'paying')  # 支付宝订单状态
            # 查询本地是否有此订单
            existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
            # 更新订单状态
            for existed_order in existed_orders:
                order_goods = existed_order.goods.all()
                for order_good in order_goods:
                    goods = order_good.goods
                    goods.sold_num += order_good.goods_num
                    goods.save()

                existed_order.pay_status = trade_status
                existed_order.trade_no = trade_no
                # existed_order.total_amount = total_amount
                existed_order.pay_time = datetime.now()
                existed_order.save()

            return Response("success")
