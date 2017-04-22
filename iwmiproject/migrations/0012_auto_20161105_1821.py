# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0011_remove_plotmanagement_water_management_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumedcrop',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='cropmonitoringplantheight',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='fertilizermanagement',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='fuelmanagement',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='gravimetricsoilmoisture',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='harvest',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='labourmanagament',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='landclearance',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='landpreparation',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='nursery',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='nurseryirrigationevent',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='pesticidemanagement',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='plantingmethod',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='plot',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='plotcultivation',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='plotirrigationevent',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='plotmanagement',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='pumpingsource',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='pumpownership',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='residuemanagement',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='saleharvestedcrop',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='soilmoisturemeasurementmanagement',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='soilmoistureprofiler',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='soilproperty',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='technologycalibration',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='technologyfailure',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='technologymanagement',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='tissuenutrientanalysis',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='weed',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='yieldfarmlevel',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='yieldplantlevel',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
        migrations.AddField(
            model_name='yieldrowbedlevel',
            name='enteredpersonel',
            field=models.ForeignKey(to='iwmiproject.SystemUser', null=True, verbose_name='Entered by', blank=True),
        ),
    ]
