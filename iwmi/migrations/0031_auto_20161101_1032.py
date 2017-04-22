# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iwmi', '0030_fertilizermanagement_s'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farm',
            options={'ordering': ['farmID']},
        ),
        migrations.RemoveField(
            model_name='farm',
            name='farmer',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='fieldID',
        ),
        migrations.AddField(
            model_name='farm',
            name='farmID',
            field=models.OneToOneField(related_name='farms', primary_key=True, serialize=False, to='iwmi.People'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farm',
            name='number',
            field=models.IntegerField(verbose_name='Total plot numbers', default=4),
        ),
    ]
