# Generated by Django 2.2.9 on 2020-03-10 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0019_remove_ordergoods_integralgood'),
    ]

    operations = [
        migrations.DeleteModel(
            name='integralgoodsCart',
        ),
    ]
