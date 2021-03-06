# Generated by Django 2.2.9 on 2020-01-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_auto_20200119_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=True, related_name='goods_catelogy', to='goods.GoodsCategoryAll', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, related_name='brandcatelogry', to='goods.GoodsCategoryAll', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=True, related_name='images', to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods/banner/', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='goodsspecification',
            name='goods',
            field=models.ForeignKey(on_delete=True, related_name='specification', to='goods.Goods', verbose_name='商品'),
        ),
    ]
