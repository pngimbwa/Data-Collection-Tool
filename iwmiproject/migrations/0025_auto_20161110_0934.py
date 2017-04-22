# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0024_waterliftingcalibration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transplanting',
            name='enteredpersonel',
        ),
        migrations.RemoveField(
            model_name='transplanting',
            name='nurseryID',
        ),
        migrations.RemoveField(
            model_name='transplanting',
            name='plotID',
        ),
        migrations.RemoveField(
            model_name='plantingmethod',
            name='planting_date',
        ),
        migrations.RemoveField(
            model_name='plantingmethod',
            name='seed_spacing_btn_a_row',
        ),
        migrations.RemoveField(
            model_name='plantingmethod',
            name='seed_spacing_within_a_row',
        ),
        migrations.RemoveField(
            model_name='plantingmethod',
            name='seeding_date',
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='date',
            field=models.DateField(null=True, blank=True, verbose_name='transplanting/seeding date'),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='nurseryID',
            field=models.ForeignKey(to='iwmiproject.Nursery', blank=True, verbose_name='nurseryID', null=True),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='plantsnumber',
            field=models.IntegerField(null=True, blank=True, verbose_name='Total number of plants transplanted'),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='plantsnumber_per_row',
            field=models.IntegerField(null=True, blank=True, verbose_name='Plant number per row'),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='spacing_btn_a_row',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant/seed spacing btn a row(cm)'),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='spacing_within_a_row',
            field=models.FloatField(null=True, blank=True, verbose_name='Plant/seed spacing within a row(cm)'),
        ),
        migrations.AlterField(
            model_name='waterliftingcalibration',
            name='plot',
            field=models.ForeignKey(to='iwmiproject.Plot', verbose_name='Plot'),
        ),
        migrations.DeleteModel(
            name='Transplanting',
        ),
    ]
