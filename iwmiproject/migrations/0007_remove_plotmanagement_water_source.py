# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0006_remove_plot_village'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmanagement',
            name='water_source',
        ),
    ]
