# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0006_instancepool_selected'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='method',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['name']},
        ),
    ]
