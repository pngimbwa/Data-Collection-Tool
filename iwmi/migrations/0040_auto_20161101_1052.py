# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0039_remove_pesticidemanagement_farm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropmonitoringplantheight',
            name='farm',
        ),
        migrations.RemoveField(
            model_name='yieldrowbedlevel',
            name='farm',
        ),
    ]
