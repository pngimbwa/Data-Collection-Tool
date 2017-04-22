# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('iwmi', '0047_auto_20161101_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, related_name='custom_user_profile', serialize=False)),
                ('firstname', models.CharField(verbose_name='First name', max_length=80)),
                ('middlename', models.CharField(verbose_name='Middle name', null=True, max_length=80, blank=True)),
                ('lastname', models.CharField(verbose_name='Last name', max_length=80)),
                ('role', models.CharField(verbose_name='Role', max_length=40)),
                ('phone', models.CharField(verbose_name='Phone', null=True, max_length=50, blank=True)),
                ('gender', models.CharField(verbose_name='Gender', max_length=10)),
                ('institution', models.CharField(verbose_name='Institution', max_length=100)),
                ('country', models.ForeignKey(verbose_name='Country', to='iwmi.Country')),
                ('village', models.ForeignKey(verbose_name='Village', to='iwmi.Village')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
