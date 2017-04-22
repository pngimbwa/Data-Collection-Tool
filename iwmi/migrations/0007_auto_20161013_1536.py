# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0006_auto_20161012_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farm',
            options={'ordering': ['fieldID']},
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='form',
            field=models.CharField(default='x', verbose_name='Form', max_length=20),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Price(Tsh)'),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='quantity_in_kg',
            field=models.FloatField(verbose_name='Quantity(Kg)', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='quantity_in_litre',
            field=models.FloatField(verbose_name='Quantity(Litre)', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='well',
            name='diameter',
            field=models.FloatField(default=0, verbose_name='Diameter(m)'),
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(verbose_name='Gender', max_length=10),
        ),
    ]
