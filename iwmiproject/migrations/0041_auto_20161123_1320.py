# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0040_cropvariety'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropVarieties',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('variety', models.CharField(verbose_name='Crop variety', max_length=70)),
                ('varietytype', models.CharField(verbose_name='Crop variety', max_length=20)),
                ('cropname', models.ForeignKey(verbose_name='Crop Name', to='iwmiproject.Crop')),
                ('plotID', models.ForeignKey(verbose_name='PlotID', to='iwmiproject.Plot')),
            ],
            options={
                'ordering': ['cropname'],
            },
        ),
        migrations.RemoveField(
            model_name='cropvariety',
            name='cropname',
        ),
        migrations.RemoveField(
            model_name='cropvariety',
            name='plotID',
        ),
        migrations.DeleteModel(
            name='CropVariety',
        ),
    ]
