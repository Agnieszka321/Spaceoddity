# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20171029_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='house',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='main_app.Planet'),
        ),
    ]