# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0045_remove_service_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='group',
        ),
    ]
