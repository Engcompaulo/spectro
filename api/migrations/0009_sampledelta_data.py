# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20160211_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampledelta',
            name='data',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
    ]