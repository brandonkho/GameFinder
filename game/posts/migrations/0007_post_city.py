# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-22 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_num_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
    ]