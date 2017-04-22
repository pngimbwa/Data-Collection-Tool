# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0012_auto_20161105_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labourmanagament',
            name='family_female_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of family female labour'),
        ),
        migrations.AlterField(
            model_name='labourmanagament',
            name='family_male_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of family male labour'),
        ),
        migrations.AlterField(
            model_name='labourmanagament',
            name='hired_female_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Numbe of hired female labour'),
        ),
        migrations.AlterField(
            model_name='labourmanagament',
            name='hired_male_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of hired male labour'),
        ),
        migrations.AlterField(
            model_name='labourmanagament',
            name='price_unit',
            field=models.CharField(blank=True, null=True, max_length=10, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='labourmanagament',
            name='wage',
            field=models.FloatField(blank=True, null=True, verbose_name='Daily wage'),
        ),
    ]
