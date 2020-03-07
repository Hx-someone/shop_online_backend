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

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(operator=request.user)

    # def get_field_queryset(self, db, db_field, request):
    #     # import ipdb;ipdb;ipdb.set_trace()
    #     qs = super().get_field_queryset(db, db_field, request)
    #     if db_field.name == "operator" and request.method == 'GET':
    #         if not qs:
    #             qs = models.User.objects.all()
    #         # 过滤数据，不显示其它APP专用配置
    #         # kwargs['widget'] = widgets.HiddenInput
    #         try:
    #             # APP专用的文件配置
    #             cf_app = qs.filter(app=request.app_id)
    #         except Exception:
    #             print('获取APP(id:%d)专用配置失败!!!' % request.app_id)
    #             cf_app = models.User.objects.none()
    #         cf_all = qs.filter(app__isnull=True)  # 所有APP通用的文件配置
    #         qs = cf_app.union(cf_all)  # 并集
    #         # print(qs, 888)
    #     return qs


admin.site.register(OrderInfo, OrderInfoAdmin)
