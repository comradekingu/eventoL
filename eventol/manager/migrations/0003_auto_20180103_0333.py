# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20180102_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='last_date',
            field=models.DateField(blank=True, default=None, help_text='Limit date to submit attendees', null=True, verbose_name='Limit Event Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='abstract',
            field=models.TextField(help_text='Short idea of the event (One or two sentences)', max_length=250, verbose_name='Abstract'),
        ),
    ]
