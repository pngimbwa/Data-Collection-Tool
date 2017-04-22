# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0184_auto_20170417_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=150)),
                ('length', models.CharField(max_length=150)),
            ],
        ),
    ]
