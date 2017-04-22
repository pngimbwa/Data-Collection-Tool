# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0172_auto_20170224_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizerspecification',
            name='nitrogen',
            field=models.FloatField(null=True, verbose_name='N content (%)', blank=True),
        ),
        migrations.AlterField(
            model_name='fertilizerspecification',
            name='organic_matter',
            field=models.FloatField(null=True, verbose_name='Organic Matter (%)', blank=True),
        ),
        migrations.AlterField(
            model_name='fertilizerspecification',
            name='phosphorus',
            field=models.FloatField(null=True, verbose_name='Phosphorus (ppm)', blank=True),
        ),
        migrations.AlterField(
            model_name='fertilizerspecification',
            name='potassium',
            field=models.FloatField(null=True, verbose_name='Potassium (ppm)', blank=True),
        ),
    ]
