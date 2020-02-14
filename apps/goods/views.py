from .serializers import *
from rest_framework import viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .filters import *


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_size_query_param = "pages"
    max_page_size = 100


class BannerListSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取轮播图列表
    """
    queryset = BannerIndex.objects.all()
    serializer_class = BannerIndexSerializer


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategoryAll.objects.all()
    serializer_class = CategorySerializer


class GoodsViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
        所有商品的信息
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    #引入filter文件里面的类，filter里面也就是过滤的字段
    filterset_class = GoodsFilter
    # 模糊检索的字段
    search_fields = ['name']
    # 排序的字段
    ordering_fields = ['sold_num', 'shop_price']