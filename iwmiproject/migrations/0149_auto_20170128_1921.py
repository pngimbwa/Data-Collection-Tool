# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0148_delete_pointofinterest'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='currency',
            field=models.CharField(blank=True, verbose_name='Currency', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='plot',
            name='lease_duration',
            field=models.FloatField(blank=True, verbose_name='Lease duration(months)', null=True),
        ),
        migrations.AddField(
            model_name='plot',
            name='payement_other',
            field=models.CharField(blank=True, verbose_name='Other payment method', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='plot',
            name='payment_monetary',
            field=models.FloatField(blank=True, verbose_name='Payment', null=True),
        ),
        migrations.AddField(
            model_name='plot',
            name='payment_option',
            field=models.CharField(blank=True, verbose_name='Payment Option', max_length=10, null=True),
        ),
    ]
