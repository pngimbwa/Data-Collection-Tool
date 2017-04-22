# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0018_auto_20161014_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('labour', models.CharField(max_length=35, verbose_name='Labour')),
                ('hired_female_number', models.IntegerField(verbose_name='Numbe of hired female labour')),
                ('hired_male_number', models.IntegerField(verbose_name='Number of hired male labour')),
                ('family_female_number', models.IntegerField(verbose_name='Number of family female labour')),
                ('family_male_number', models.IntegerField(verbose_name='Number of family male labour')),
                ('activity', models.CharField(max_length=100, verbose_name='Performed activity')),
                ('wage', models.FloatField(verbose_name='Wage')),
                ('farm', models.ForeignKey(to='iwmi.Farm', verbose_name='Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
