# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_auto_20171024_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='rating_avg',
            field=models.FloatField(null=True),
        ),
    ]
