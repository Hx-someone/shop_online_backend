# Generated by Django 2.2.9 on 2020-03-07 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0011_orderinfo_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='operator',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=True, related_name='operator', to=settings.AUTH_USER_MODEL, verbose_name='订单配送人员'),
        ),
    ]
