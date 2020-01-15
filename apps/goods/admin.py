from django.contrib import admin
from .models import *
# Register your models here.


class GoodsCategoryAllAdmin(admin.ModelAdmin):
    pass


class GoodsAdmin(admin.ModelAdmin):
    pass


class GoodsImageAdmin(admin.ModelAdmin):
    pass


class BannerAdmin(admin.ModelAdmin):
    pass


class BannerIndexAdmin(admin.ModelAdmin):
    pass


class GoodsCategoryBrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(GoodsCategoryAll,GoodsCategoryAllAdmin)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(GoodsImage,GoodsImageAdmin)
admin.site.register(Banner,BannerAdmin)
admin.site.register(BannerIndex,BannerIndexAdmin)
admin.site.register(GoodsCategoryBrand,GoodsCategoryBrandAdmin)