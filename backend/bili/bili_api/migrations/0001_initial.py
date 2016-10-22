# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-22 21:00
from __future__ import unicode_literals

import bili_api.models.ads
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='publish date')),
                ('active_since', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True)),
                ('category', models.CharField(choices=[('Cars', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Property', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('Clothing', 'clothing')], default='ab', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AdImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=bili_api.models.ads.AdImage.user_directory_path)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bili_api.Ad')),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bili_api.Ad')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bili_api.Person')),
            ],
        ),
        migrations.AddField(
            model_name='favourites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bili_api.Person'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bili_api.Person'),
        ),
        migrations.AddField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bili_api.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='favourites',
            unique_together=set([('user', 'ad')]),
        ),
    ]
