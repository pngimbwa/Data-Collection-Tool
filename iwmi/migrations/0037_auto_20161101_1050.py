# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0036_auto_20161101_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='furrow',
            options={'ordering': ['plotID']},
        ),
        migrations.RemoveField(
            model_name='furrow',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='technologycalibration',
            name='farmer',
        ),
        migrations.RemoveField(
            model_name='technologyfailure',
            name='farmer',
        ),
        migrations.RemoveField(
            model_name='technologymanagement',
            name='farmer',
        ),
        migrations.AddField(
            model_name='technologycalibration',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Farm', to='iwmi.Farm'),
        ),
        migrations.AddField(
            model_name='technologyfailure',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Farm', to='iwmi.Farm'),
        ),
        migrations.AddField(
            model_name='technologymanagement',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Farm', to='iwmi.Farm'),
        ),
        migrations.AlterField(
            model_name='technologycalibration',
            name='bucketvolume',
            field=models.FloatField(blank=True, null=True, verbose_name='Bucket volume (litre)'),
        ),
        migrations.AlterField(
            model_name='technologycalibration',
            name='discharge',
            field=models.FloatField(blank=True, null=True, verbose_name='Discharge(m3/s)'),
        ),
    ]
