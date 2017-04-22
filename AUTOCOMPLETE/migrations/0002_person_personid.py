# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('AUTOCOMPLETE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='personID',
            field=models.CharField(blank=True, unique=True, default=uuid.uuid4, max_length=100),
        ),
    ]
