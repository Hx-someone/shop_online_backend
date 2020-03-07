from django.contrib import admin
from .models import *
# from guardian.admin import GuardedModelAdmin


# Register your models here.


class OrderGoodsInline(admin.StackedInline):
    model = OrderGoods
    extra = 0


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['order_sn', 'order_mount', 'operator']
    inlines = (OrderGoodsInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(operator=request.user)


admin.site.register(OrderInfo, OrderInfoAdmin)
