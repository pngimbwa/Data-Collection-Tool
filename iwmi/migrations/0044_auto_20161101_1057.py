# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0043_remove_soilproperty_farm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gravimetricsoilmoisture',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='farm',
        ),
    ]
