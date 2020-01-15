from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
        用户表，是继承Django默认的user表，再做出修改
    """
    name=models.CharField(max_length=30,null=True,blank=True,verbose_name="昵称")
    gender=models.CharField(max_length=6,choices=(("male","男"),("female","女")),default="male",verbose_name="性别")
    integral=models.IntegerField(default=0,verbose_name="积分")
    mobile=models.CharField(max_length=11,verbose_name="电话",null=True,blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
        短信验证码
    """
    code=models.CharField(max_length=10,verbose_name="验证码")
    mobile=models.CharField(max_length=11,verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code