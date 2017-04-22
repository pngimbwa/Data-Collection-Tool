# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0033_auto_20161101_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlotOperation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date activity was performed')),
                ('activity', models.TextField(max_length=200, verbose_name='Activity')),
                ('number', models.IntegerField(verbose_name='Number of people')),
                ('plotID', models.ForeignKey(to='iwmi.Plot', verbose_name='PlotID')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='farmoperation',
            name='farm',
        ),
        migrations.DeleteModel(
            name='FarmOperation',
        ),
    ]
