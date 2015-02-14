# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycubewars', '0004_auto_20150201_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('create_date', models.DateTimeField()),
                ('accountID', models.ForeignKey(to='mycubewars.Account')),
                ('characterID', models.ForeignKey(to='mycubewars.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
