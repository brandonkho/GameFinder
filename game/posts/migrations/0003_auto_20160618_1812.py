# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-19 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160618_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='sport',
            field=models.CharField(choices=[('basketball', 'Basketball'), ('soccer', 'Soccer'), ('volleyball', 'Volleyball'), ('frisbee', 'Ultimate Frisbee'), ('tennis', 'Tennis')], max_length=20),
        ),
    ]
