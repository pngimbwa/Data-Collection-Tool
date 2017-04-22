# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0028_auto_20161026_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterSourceCategory',
            fields=[
                ('category', models.CharField(serialize=False, max_length=50, primary_key=True, verbose_name='Pumping Source')),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='WaterSources',
            fields=[
                ('ID', models.CharField(serialize=False, max_length=10, primary_key=True, verbose_name='Water source ID')),
                ('name', models.CharField(max_length=50, verbose_name='Water source type')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='watersourcecategory',
            name='watersourcetype',
            field=models.ForeignKey(to='iwmi.WaterSources', verbose_name='Water source type'),
        ),
    ]
