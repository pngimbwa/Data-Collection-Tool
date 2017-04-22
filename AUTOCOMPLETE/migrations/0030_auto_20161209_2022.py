# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOCOMPLETE', '0029_auto_20161209_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personID',
            field=models.CharField(blank=True, default='8BF809', max_length=100, unique=True),
        ),
    ]
