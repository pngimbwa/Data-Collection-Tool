# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0016_remove_nursery_date_trasplanting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labourmanagament',
            old_name='plotID',
            new_name='areaID',
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='areadescription',
            field=models.CharField(max_length=35, null=True, verbose_name='Area description', blank=True),
        ),
    ]
