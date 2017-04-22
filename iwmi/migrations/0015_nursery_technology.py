# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0014_auto_20161014_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='nursery',
            name='technology',
            field=models.ForeignKey(verbose_name='Calibrated Technology', blank=True, null=True, to='iwmi.Technology'),
        ),
    ]
