# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0012_auto_20161013_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmFields',
            fields=[
                ('farmID', models.CharField(max_length=40, verbose_name='FarmID', serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['farmID'],
            },
        ),
        migrations.RemoveField(
            model_name='farm',
            name='crop',
        ),
        migrations.AddField(
            model_name='farm',
            name='crop',
            field=models.ForeignKey(to='iwmi.Crop', verbose_name='Crop(s)', default='g'),
        ),
        migrations.AddField(
            model_name='farmfields',
            name='fields',
            field=models.ManyToManyField(verbose_name='Field(s)', to='iwmi.Farm'),
        ),
    ]
