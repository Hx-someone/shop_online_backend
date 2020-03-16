# Generated by Django 2.2.9 on 2020-03-16 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0046_auto_20200316_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integralgoodscart',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Integralgoods', verbose_name='积分兑换商品'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='delivery_time',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='订单配送时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='distributor_time',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='订单分配时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='inspecter_time',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='订单二次验货时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='picker_time',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='订单拣货时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='success_time',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='交易完成时间'),
        ),
        migrations.AlterField(
            model_name='orderintergralgoods',
            name='inter_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Integralgoods', verbose_name='积分商品'),
        ),
    ]
