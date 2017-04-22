# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0062_pumpingsource_elevation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labourmanagament',
            name='time_taken',
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='family_female_time',
            field=models.FloatField(null=True, blank=True, verbose_name='Time taken for family female'),
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='family_male_time',
            field=models.FloatField(null=True, blank=True, verbose_name='Time taken fo family male'),
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='hired_female_time',
            field=models.FloatField(null=True, blank=True, verbose_name='Time taken for hired female'),
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='hired_male_time',
            field=models.FloatField(null=True, blank=True, verbose_name='Time taken for hired male'),
        ),
    ]
