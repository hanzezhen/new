# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-05-28 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yuyue',
            name='isquxiao',
            field=models.BooleanField(default=False, verbose_name='取消'),
        ),
    ]
