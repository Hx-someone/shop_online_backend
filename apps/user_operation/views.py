from rest_framework import viewsets
from rest_framework import mixins
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# from .models import UserFav, UserLeavingMessage, UserAddress
from utils.permissions import IsOwnerOrReadOnly
# from .serializers import UserFavSerializer, UserFavDetailSerializer, AddressSerializer, LeavingMessageSerializer


class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    #这个是用户信息的收藏函数，如果有人收藏了商品，这个商品的收藏数就+1
    """
    list:
        获取用户收藏列表
    retrieve:
        判断某个商品是否已经收藏
    create:
        收藏商品
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     goods = instance.goods
    #     goods.fav_num += 1
    #     goods.save()

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer


class AddressViewset(viewsets.ModelViewSet):
    # 这个是用户的地址栏，ModelViewSet可以对商品进行增删改查，get_queryset就是可以对于一个视频
    """
    收货地址管理
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
