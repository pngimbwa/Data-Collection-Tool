# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0088_remove_otherwaterusage_plot'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedplot',
            name='farm',
            field=models.ForeignKey(blank=True, verbose_name='Farm', null=True, to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='farm',
            field=models.ForeignKey(blank=True, verbose_name='Farm', null=True, to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='furrow',
            name='farm',
            field=models.ForeignKey(blank=True, verbose_name='Farm', null=True, to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='pesticidemanagement',
            name='farm',
            field=models.ForeignKey(blank=True, verbose_name='Farm', null=True, to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='plotcropproperty',
            name='farm',
            field=models.ForeignKey(blank=True, verbose_name='Farm', null=True, to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='plotcultivation',
            name='farm',
            field=models.ForeignKey(blank=True, verbose_name='Farm(s)', null=True, to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='plotoperation',
            name='farm',
            field=models.ForeignKey(blank=True, verbose_name='Farm(s)', null=True, to='iwmiproject.Farm'),
        ),
        migrations.AddField(
            model_name='watermanagement',
            name='farm',
            field=models.ForeignKey(blank=True, verbose_name='Farm(s)', null=True, to='iwmiproject.Farm'),
        ),
    ]
