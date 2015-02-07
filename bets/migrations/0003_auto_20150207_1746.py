# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0002_auto_20150207_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betroom',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
