# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-06-29 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20220630_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
