# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0174_plot_fieldtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='fieldtype',
            field=models.CharField(verbose_name='Fieldtype', blank=True, null=True, max_length=20),
        ),
    ]
