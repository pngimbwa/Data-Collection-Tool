# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0085_auto_20161206_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('stress', models.CharField(blank=True, null=True, max_length=25, verbose_name='Stress')),
                ('severness', models.CharField(blank=True, null=True, max_length=8, verbose_name='Severness')),
                ('farm', models.ForeignKey(to='iwmiproject.Farm', verbose_name='Farm')),
                ('plot', models.ForeignKey(to='iwmiproject.Plot', verbose_name='Plot')),
            ],
        ),
    ]
