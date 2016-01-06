# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160106_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='tag',
        ),
        migrations.AddField(
            model_name='repository',
            name='tag',
            field=models.ManyToManyField(blank=True, default='', to='blog.Tag'),
        ),
    ]