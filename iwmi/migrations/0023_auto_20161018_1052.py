# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0022_auto_20161017_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabourManagament',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('labour', models.CharField(max_length=35, verbose_name='Labour')),
                ('hired_female_number', models.IntegerField(verbose_name='Numbe of hired female labour')),
                ('hired_male_number', models.IntegerField(verbose_name='Number of hired male labour')),
                ('family_female_number', models.IntegerField(verbose_name='Number of family female labour')),
                ('family_male_number', models.IntegerField(verbose_name='Number of family male labour')),
                ('activity', models.CharField(max_length=100, verbose_name='Performed activity')),
                ('wage', models.FloatField(verbose_name='Wage')),
                ('farm', models.ForeignKey(verbose_name='Farm', to='iwmi.Farm')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='labour',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='pesticidemanagement',
            name='personels',
        ),
        migrations.DeleteModel(
            name='Labour',
        ),
    ]
