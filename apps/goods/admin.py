from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class GoodsCategoryAllResource(resources.ModelResource):
    class Meta:
        model = GoodsCategoryAll


@admin.register(GoodsCategoryAll)
class ProxyAdmin(ImportExportModelAdmin):
    resource_class = GoodsCategoryAllResource


class GoodImageInline(admin.StackedInline):
    model = GoodsImage
    extra = 1   #默认是3个


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['category','name','fav_num','goods_num','history_price','shop_price','goods_front_image','Specifications','is_new','is_hot','is_normal','add_time']
    search_fields = ['name','fav_num','goods_num','history_price','shop_price']
    inlines = (GoodImageInline,)


admin.site.register(Goods,GoodsAdmin)
admin.site.register(BannerIndex)
admin.site.register(GoodsCategoryBrand)