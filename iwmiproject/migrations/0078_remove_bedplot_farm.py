# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0077_bedplot_farm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bedplot',
            name='farm',
        ),
    ]
