from django.contrib import admin
from .models import *
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    pass


class VerifyCodeAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(VerifyCode,VerifyCodeAdmin)
