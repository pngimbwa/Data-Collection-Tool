# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0039_auto_20161122_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropVariety',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('variety', models.CharField(max_length=70, verbose_name='Crop variety')),
                ('varietytype', models.CharField(max_length=20, verbose_name='Crop variety')),
                ('cropname', models.ForeignKey(to='iwmiproject.Crop', verbose_name='Crop Name')),
                ('plotID', models.ForeignKey(to='iwmiproject.Plot', verbose_name='PlotID')),
            ],
            options={
                'ordering': ['cropname'],
            },
        ),
    ]
