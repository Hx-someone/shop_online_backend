# Generated by Django 2.2.9 on 2020-03-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200115_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='isfaith',
            field=models.BooleanField(default=False, verbose_name='是否违约'),
        ),
    ]
