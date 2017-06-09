# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170609_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='post_tags', to='posts.InterestTag'),
        ),
    ]