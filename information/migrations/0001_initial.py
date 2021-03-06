# Generated by Django 2.2.9 on 2020-03-16 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileVisitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问总次数')),
            ],
            options={
                'verbose_name': '移动端访问总次数',
                'verbose_name_plural': '移动端访问总次数',
            },
        ),
        migrations.CreateModel(
            name='PCVisitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问总次数')),
            ],
            options={
                'verbose_name': 'PC网站访问总次数',
                'verbose_name_plural': 'PC网站访问总次数',
            },
        ),
    ]
