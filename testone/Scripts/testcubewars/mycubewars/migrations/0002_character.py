# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycubewars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('create_date', models.DateTimeField()),
                ('level', models.IntegerField()),
                ('artist', models.ForeignKey(to='mycubewars.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
