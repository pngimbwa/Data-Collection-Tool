# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0123_remove_plotmanagement_seasonend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmanagement',
            name='growinglength',
        ),
    ]
