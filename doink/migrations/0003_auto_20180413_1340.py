# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doink', '0002_auto_20180413_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='both',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='innerclass',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neither',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
