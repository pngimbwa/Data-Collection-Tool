# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0108_auto_20161222_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='total_irrigated_plots',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='total_irrigated_plots_land_area',
        ),
        migrations.AddField(
            model_name='farm',
            name='irrigated_plots',
            field=models.FloatField(null=True, verbose_name='Total irrigated rented land(hactre)', blank=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='landownership',
            field=models.CharField(null=True, verbose_name='Landownership', max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='owned_land',
            field=models.FloatField(null=True, verbose_name='Owned land(hactre)', blank=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='rented_land',
            field=models.FloatField(null=True, verbose_name='rented land(hactre)', blank=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='total_irrigated_owned_land',
            field=models.FloatField(null=True, verbose_name='Total irrigated owned land(hactre)', blank=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='total_irrigated_rented_land',
            field=models.FloatField(null=True, verbose_name='Field Size (hactre)', blank=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='fieldsize',
            field=models.FloatField(verbose_name='Field Size (hactre)'),
        ),
    ]
