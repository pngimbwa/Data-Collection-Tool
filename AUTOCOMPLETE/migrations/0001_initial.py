# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyStation',
            fields=[
                ('name', models.CharField(verbose_name='Name', max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(verbose_name='Name', max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(verbose_name='Name', max_length=50, primary_key=True, serialize=False)),
                ('birth_country', models.ForeignKey(to='AUTOCOMPLETE.Country', verbose_name='country')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='companystation',
            name='countries',
            field=models.ManyToManyField(to='AUTOCOMPLETE.Country', verbose_name='country'),
        ),
    ]
