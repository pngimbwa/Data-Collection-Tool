# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0117_auto_20161230_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantingmethod',
            name='date',
        ),
        migrations.RemoveField(
            model_name='plantingmethod',
            name='plantsnumber_per_row',
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='CroppingSystem',
            field=models.CharField(verbose_name='Planting Method', blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='date_one',
            field=models.DateField(verbose_name='transplanting/seeding date for crop One', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='date_two',
            field=models.DateField(verbose_name='transplanting/seeding date for crop two', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='plantsnumber_per_row_one',
            field=models.IntegerField(verbose_name='Plant number per row for crop one', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='plantsnumber_per_row_two',
            field=models.IntegerField(verbose_name='Plant number per row for crop two', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='seed_quantity2',
            field=models.FloatField(verbose_name='seeding quantity for crop two', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='spacing_within_a_row_two',
            field=models.FloatField(verbose_name='Plant/seed spacing within a row for second crop(cm)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantingmethod',
            name='planting_method',
            field=models.CharField(verbose_name='Planting Method', blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='plantingmethod',
            name='seed_quantity',
            field=models.FloatField(verbose_name='seeding quantity for crop one', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plantingmethod',
            name='spacing_within_a_row',
            field=models.FloatField(verbose_name='Plant/seed spacing within a row for first crop(cm)', blank=True, null=True),
        ),
    ]
