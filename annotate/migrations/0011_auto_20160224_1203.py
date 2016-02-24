# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 17:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('annotate', '0010_task_assigned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned',
        ),
        migrations.AddField(
            model_name='task',
            name='assignedTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]