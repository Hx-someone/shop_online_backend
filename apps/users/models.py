from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
        用户表，是继承Django默认的user表，再做出修改
    """
    status = (('primary','初级会员'),('senior','高级会员'))
    role_status=(('ordinary_user','普通用户'),('order_distributor','订单分配员'),('picker','商品拣货员'),('delivery','送货员'),('shop_inspector','超市自提商品管理员'),('manager','后台管理员'),('boss','超级管理员'))
    name=models.CharField(max_length=30,null=True,blank=True,verbose_name="昵称")
    avatar = models.ImageField(upload_to="avatar/",default='avatar/default.png', blank=True, null=True)
    member_status = models.CharField(max_length=30,choices=status,default='primary',verbose_name="会员等级")
    gender=models.CharField(max_length=6,choices=(("male","男"),("female","女")),default="male",verbose_name="性别")
    role = models.CharField(max_length=30,choices=role_status,default='ordinary_user',verbose_name='角色')
    integral=models.IntegerField(default=0,verbose_name="积分")
    isfaith = models.BooleanField(default=False,verbose_name='是否违约')
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