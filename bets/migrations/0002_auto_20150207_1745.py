# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_id', models.CharField(max_length=255)),
                ('to_id', models.CharField(max_length=255)),
                ('bet_type', models.CharField(max_length=20, choices=[(b'PAY_IN', b'Pay In'), (b'PAY_OUT', b'Pay Out')])),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BetRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(verbose_name=b'datecreated')),
                ('password', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
                ('url', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option_name', models.CharField(max_length=255)),
                ('betroom', models.ForeignKey(related_name='options', to='bets.BetRoom')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='bet',
            name='bet_option',
            field=models.ForeignKey(related_name='transactions', to='bets.Option'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bet',
            name='betroom_id',
            field=models.ForeignKey(related_name='bets', to='bets.BetRoom'),
            preserve_default=True,
        ),
    ]
