# Generated by Django 2.2.9 on 2020-03-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0012_auto_20200307_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('paying', '待支付'), ('TRADE_SUCCESS', '成功'), ('refunding', '退款申请中'), ('fefunding', '退款成功，交易结束'), ('Picking', '订单商品配货中'), ('checkout', '商品正在进行第二次检验'), ('TRADE_FINISHED', '交易结束'), ('Delivery', '订单商品送货中')], default='paying', max_length=30, verbose_name='订单状态'),
        ),
    ]
