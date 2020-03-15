# Generated by Django 2.2.9 on 2020-03-15 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0037_auto_20200315_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='distributor',
            field=models.CharField(default='', max_length=20, verbose_name='订单分配员'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='inspecter',
            field=models.CharField(default='', max_length=20, verbose_name='订单二次拣货人'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='picker',
            field=models.CharField(default='', max_length=20, verbose_name='订单拣货人'),
        ),
        migrations.AlterField(
            model_name='integralgoodscart',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Integralgoods', verbose_name='积分兑换商品'),
        ),
        migrations.AlterField(
            model_name='orderintergralgoods',
            name='inter_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Integralgoods', verbose_name='积分商品'),
        ),
    ]
