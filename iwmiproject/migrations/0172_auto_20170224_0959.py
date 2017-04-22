# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iwmiproject', '0171_auto_20170222_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='FertilizerSpecification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nitrogen', models.FloatField(verbose_name='N content (%)')),
                ('phosphorus', models.FloatField(verbose_name='Phosphorus (ppm)')),
                ('potassium', models.FloatField(verbose_name='Potassium (ppm)')),
                ('sulphur', models.FloatField(verbose_name='Sulphur(g/kg)', blank=True, null=True)),
                ('organic_matter', models.FloatField(verbose_name='Organic Matter (%)')),
                ('enteredpersonel', models.ForeignKey(verbose_name='Entered by', to='iwmiproject.SystemUser', blank=True, null=True)),
                ('farm', models.ForeignKey(verbose_name='Farm', to='iwmiproject.Farm', blank=True, null=True)),
                ('fertilizer', models.ForeignKey(verbose_name='Fertilizer', to='iwmiproject.Fertilizer')),
                ('plotID', models.ForeignKey(verbose_name='Plot ID', to='iwmiproject.Plot', blank=True, null=True)),
            ],
            options={
                'ordering': ['plotID'],
            },
        ),
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='nitrogen',
        ),
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='organic_matter',
        ),
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='phosphorus',
        ),
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='fertilizermanagement',
            name='sulphur',
        ),
    ]
