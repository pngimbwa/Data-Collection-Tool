# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0125_plotirrigationevent_service_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantingmethod',
            name='CroppingSystem',
            field=models.CharField(null=True, max_length=20, blank=True, verbose_name='Cropping System'),
        ),
        migrations.AlterField(
            model_name='plantingmethod',
            name='nurseryID_one',
            field=models.CharField(null=True, max_length=45, blank=True, verbose_name='nurseryID for Crop One'),
        ),
        migrations.AlterField(
            model_name='plantingmethod',
            name='nurseryID_two',
            field=models.CharField(null=True, max_length=45, blank=True, verbose_name='nurseryID for Crop Two'),
        ),
    ]
