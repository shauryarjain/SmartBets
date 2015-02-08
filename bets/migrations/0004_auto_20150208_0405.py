# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0003_auto_20150207_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='amount',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bet',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='betroom',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
    ]
