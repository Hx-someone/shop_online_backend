from datetime import datetime

from django.db import models
from users.models import UserProfile
# Create your models here.


class GoodsCategoryAll(models.Model):
    """
    商品类别
    """
    name = models.CharField(default='',max_length=30,verbose_name="类别名",help_text="类别名")
    image = models.ImageField(upload_to="category/", verbose_name="类别图片", null=True, blank=True)
    icon = models.ImageField(upload_to="icon/",verbose_name="图标",null=True,blank=True)
    is_show = models.BooleanField(default=False,verbose_name="是否放在首页分类展示")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    category = models.ForeignKey(GoodsCategoryAll, related_name='brands', null=True, blank=True, verbose_name="商品类目",on_delete=True)
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/")
    is_hot = models.BooleanField(default=False,verbose_name="是否放上品牌特卖")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategoryAll, verbose_name="商品类目",related_name="catelogys",on_delete=True)
    name = models.CharField(max_length=100, verbose_name="商品名")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    history_price = models.FloatField(verbose_name="促销价格",blank=True,null=True)
    shop_price = models.FloatField(default=0, verbose_name="当前价格")
    Specifications=models.CharField(default='',verbose_name="商品规格",max_length=30)
    Storage_type = models.CharField(default="常温",verbose_name="存储方式",max_length=30)
    goods_brief = models.TextField(max_length=500, verbose_name="商品描述")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否放上新品栏")      #后期要删掉
    is_hot = models.BooleanField(default=True, verbose_name="是否放上首页热销栏")
    is_normal=models.BooleanField(default=True,verbose_name="是否为上架商品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images",on_delete=True)
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class BannerIndex(models.Model):
    """
    首页轮播
    """
    name = models.CharField(default='',verbose_name="轮播图名字",max_length=30)
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '首页轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
