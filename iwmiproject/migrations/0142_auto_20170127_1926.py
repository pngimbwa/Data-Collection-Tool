# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0141_auto_20170127_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmanagement',
            name='management_practice',
        ),
        migrations.RemoveField(
            model_name='plotmanagement',
            name='mulching_quantity',
        ),
        migrations.RemoveField(
            model_name='plotmanagement',
            name='mulching_type',
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop1_management_practice',
            field=models.CharField(verbose_name='Crop one Management practice', blank=True, null=True, max_length=10),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop1_mulching_quantity',
            field=models.FloatField(verbose_name='Crop one Mulching quantity', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop1_mulching_type',
            field=models.CharField(verbose_name='Crop one Mulching type', blank=True, null=True, max_length=45),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop1_rootdepth',
            field=models.FloatField(verbose_name='Crop one rootdepth(m)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop2_management_practice',
            field=models.CharField(verbose_name='Crop two management practice', blank=True, null=True, max_length=10),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop2_mulching_quantity',
            field=models.FloatField(verbose_name='Crop two mulching quantity', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop2_mulching_type',
            field=models.CharField(verbose_name='Crop two mulching type', blank=True, null=True, max_length=45),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='crop2_rootdepth',
            field=models.FloatField(verbose_name='Crop two rootdepth(m)', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plotcrop',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', verbose_name='Entered by', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop1_planting_method',
            field=models.CharField(verbose_name='Crop one planting Method', blank=True, null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop1_variety',
            field=models.CharField(verbose_name='Crop one variety', blank=True, null=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop1_varietytype',
            field=models.CharField(verbose_name='Crop one variety Type', blank=True, null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop2_planting_method',
            field=models.CharField(verbose_name='Crop two planting Method', blank=True, null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop2_variety',
            field=models.CharField(verbose_name='Crop two variety', blank=True, null=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='plotcrop',
            name='crop2_varietytype',
            field=models.CharField(verbose_name='Crop two variety Type', blank=True, null=True, max_length=20),
        ),
    ]
