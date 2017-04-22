# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0161_auto_20170209_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel2',
            fields=[
                ('hostelID', models.IntegerField(serialize=False, primary_key=True)),
                ('hostelname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='House2',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('housename', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='hostel2',
            name='house',
            field=models.ForeignKey(to='iwmiproject.House2'),
        ),
    ]
