# Generated by Django 2.2.9 on 2020-03-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_isfaith'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='isfaith',
            field=models.BooleanField(default=True, verbose_name='是否违约'),
        ),
    ]
