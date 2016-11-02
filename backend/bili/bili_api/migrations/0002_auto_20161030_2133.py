# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-30 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bili_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='bili_api.Person'),
        ),
    ]
