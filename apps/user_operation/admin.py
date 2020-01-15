from django.contrib import admin
from .models import *
# Register your models here.


class UserFavAdmin(admin.ModelAdmin):
    pass


class UserAddressAdmin(admin.ModelAdmin):
    pass


class integral_calculationAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserFav,UserFavAdmin)
admin.site.register(UserAddress,UserAddressAdmin)
admin.site.register(integral_calculation,integral_calculationAdmin)
