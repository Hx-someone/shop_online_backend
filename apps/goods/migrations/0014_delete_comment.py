# Generated by Django 2.2.9 on 2020-03-07 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0013_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
