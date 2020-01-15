from rest_framework import serializers
from .models import *


class BannerIndexSerializer(serializers.ModelSerializer):
    """
        首页的轮播图
    """
    class Meta:
        model = BannerIndex
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
        这个是商品分类的序列化，但是为了让商品分类里面可以显示商品的信息，所以要吧商品序列化的结果作为商品分类的一个字段
    """
    class Meta:
        model = GoodsCategoryAll
        fields = "__all__"