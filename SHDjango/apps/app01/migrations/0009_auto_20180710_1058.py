# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20180709_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artsuser',
            name='flag',
            field=models.IntegerField(choices=[(0, '普通会员'), (1, '白银会员'), (2, '黄金会员')], default=0, verbose_name='控制字段'),
        ),
    ]