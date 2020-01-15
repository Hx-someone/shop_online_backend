from django.contrib import admin
from .models import *
# Register your models here.


class ShoppingCartAdmin(admin.ModelAdmin):
    pass


class OrderInfoAdmin(admin.ModelAdmin):
    pass


class OrderGoodsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShoppingCart,ShoppingCartAdmin)
admin.site.register(OrderInfo,OrderInfoAdmin)
admin.site.register(OrderGoods,OrderGoodsAdmin)
