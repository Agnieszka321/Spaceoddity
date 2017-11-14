# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20171029_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='house_photo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='description_long',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='main_photo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planet',
            name='small_photo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]