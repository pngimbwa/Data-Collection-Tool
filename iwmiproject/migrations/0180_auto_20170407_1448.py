# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0179_auto_20170227_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement',
        ),
        migrations.RemoveField(
            model_name='tdrmeasurement',
            name='measurement_depth',
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_eigth',
            field=models.FloatField(blank=True, null=True, verbose_name='Eighth Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_five',
            field=models.FloatField(blank=True, null=True, verbose_name='Fifth Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_four',
            field=models.FloatField(blank=True, null=True, verbose_name='Fourth Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_nine',
            field=models.FloatField(blank=True, null=True, verbose_name='Ninth Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_one',
            field=models.FloatField(blank=True, null=True, verbose_name='First Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_seven',
            field=models.FloatField(blank=True, null=True, verbose_name='Seventh Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_six',
            field=models.FloatField(blank=True, null=True, verbose_name='Sixth Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_ten',
            field=models.FloatField(blank=True, null=True, verbose_name='Tenth Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_three',
            field=models.FloatField(blank=True, null=True, verbose_name='Third Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_depth_two',
            field=models.FloatField(blank=True, null=True, verbose_name='Second Measurement depth (cm)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_eigth',
            field=models.FloatField(blank=True, null=True, verbose_name='Eighth Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_five',
            field=models.FloatField(blank=True, null=True, verbose_name='Fifth Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_four',
            field=models.FloatField(blank=True, null=True, verbose_name='Fourth Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_nine',
            field=models.FloatField(blank=True, null=True, verbose_name='Ninth Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_one',
            field=models.FloatField(blank=True, null=True, verbose_name='First Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_seven',
            field=models.FloatField(blank=True, null=True, verbose_name='Seventh Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_six',
            field=models.FloatField(blank=True, null=True, verbose_name='Sixth Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_ten',
            field=models.FloatField(blank=True, null=True, verbose_name='Tenth Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_three',
            field=models.FloatField(blank=True, null=True, verbose_name='Third Measurement(%)'),
        ),
        migrations.AddField(
            model_name='tdrmeasurement',
            name='measurement_two',
            field=models.FloatField(blank=True, null=True, verbose_name='Second Measurement(%)'),
        ),
    ]
