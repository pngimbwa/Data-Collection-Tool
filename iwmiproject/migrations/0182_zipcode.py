# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0181_auto_20170407_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('zipcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=64)),
                ('statecode', models.CharField(max_length=2)),
                ('statename', models.CharField(max_length=32)),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['zipcode'],
            },
        ),
    ]
