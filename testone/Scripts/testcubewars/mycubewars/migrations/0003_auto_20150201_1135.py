# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycubewars', '0002_character'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='artist',
            new_name='account',
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
