# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0020_auto_20180711_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='artsuser',
            name='telephon_check',
            field=models.CharField(max_length=20, null=True, verbose_name='短信验证码'),
        ),
    ]
