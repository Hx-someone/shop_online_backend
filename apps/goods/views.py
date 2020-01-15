from .serializers import *
from rest_framework import viewsets
from rest_framework import mixins


class BannerListSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取轮播图列表
    """
    queryset = BannerIndex.objects.all()
    serializer_class = BannerIndexSerializer


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    # filterset_fields是模糊检索name（分类名字字段）
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategoryAll.objects.all()
    serializer_class = CategorySerializer
