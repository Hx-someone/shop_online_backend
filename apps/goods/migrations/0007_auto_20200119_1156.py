# Generated by Django 2.2.9 on 2020-01-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20200119_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsspecification',
            options={'verbose_name': '商品规格', 'verbose_name_plural': '商品规格'},
        ),
        migrations.AddField(
            model_name='goodsspecification',
            name='price',
            field=models.CharField(default=21, max_length=100, verbose_name='商品价格'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=True, to='goods.GoodsCategoryAll', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='goods.GoodsCategoryAll', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(on_delete=True, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='goodsspecification',
            name='goods',
            field=models.ForeignKey(on_delete=True, to='goods.Goods', verbose_name='商品'),
        ),
    ]