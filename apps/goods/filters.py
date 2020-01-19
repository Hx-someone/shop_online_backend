import django_filters
from django.db.models import Q
from .models import *


class GoodsFilter(django_filters.rest_framework.FilterSet):
    min_price = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    is_new = django_filters.BooleanFilter(field_name="is_new")
    is_hot = django_filters.BooleanFilter(field_name="is_hot")
    is_normal = django_filters.BooleanFilter(field_name="is_normal")
    category_type = django_filters.NumberFilter(field_name="category")

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'is_new', 'is_normal', 'is_hot', 'category_type']