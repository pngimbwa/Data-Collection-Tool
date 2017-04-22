# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0049_auto_20161123_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidualHandling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(verbose_name='Weeding date')),
                ('residual_activities', models.CharField(verbose_name='What they do', max_length=80)),
                ('time', models.FloatField(verbose_name='Time taken')),
                ('enteredpersonel', models.ForeignKey(verbose_name='Entered by', null=True, to='iwmiproject.SystemUser', blank=True)),
                ('plotID', models.ForeignKey(verbose_name='PlotID', null=True, to='iwmiproject.Plot', blank=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
