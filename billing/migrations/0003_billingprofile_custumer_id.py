# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-30 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20191219_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingprofile',
            name='custumer_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
