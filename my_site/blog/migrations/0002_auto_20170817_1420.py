# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 14:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publish_date',
            new_name='published_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 17, 14, 20, 8, 133738, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 17, 14, 20, 8, 133087, tzinfo=utc)),
        ),
    ]
