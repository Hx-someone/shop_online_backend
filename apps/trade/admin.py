from django.contrib import admin
from .models import *


# from guardian.admin import GuardedModelAdmin


# Register your models here.


class OrderGoodsInline(admin.StackedInline):
    model = OrderGoods
    extra = 0


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['order_sn', 'order_mount', 'operator','operator_phone','takegoods_status','pay_status']
    list_filter = ['order_sn','order_mount']
    search_fields = ['takegoods_status','pay_status']
    inlines = (OrderGoodsInline,)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            user = form.save()
            if user.operator:
                user.operator_phone = user.operator.mobile
            else:
                return
            user.save()
        super().save_model(request,obj,form,change)

    # def get_readonly_fields(self, request, obj=None):
    #     fields = []
    #     if request.user.is_superuser:
    #         return fields
    #     else:
    #         fields = ['order_sn', 'order_mount','takegoods_status']
    #         return fields

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "pay_status":
            usuario_id = request.GET.get('pay_status_id', None)
            if usuario_id:
                kwargs['initial'] = usuario_id
        if db_field.name == "pay_status":
            kwargs["queryset"] = User.objects.filter(is_superuser=True)
        return super(OrderInfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(operator=request.user)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "operator":
    #         kwargs["queryset"] = User.objects.filter(user=request.user)
    #     return super(OrderInfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(OrderInfo, OrderInfoAdmin)
admin.site.register(IntegralgoodsCart)
