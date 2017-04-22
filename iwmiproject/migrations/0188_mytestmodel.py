# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0187_delete_mytestmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTestModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('length', models.FloatField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
