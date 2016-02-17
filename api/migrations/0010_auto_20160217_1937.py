# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_sampledelta_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samplefeature',
            name='sharpness',
        ),
        migrations.AddField(
            model_name='samplefeature',
            name='frequency',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
