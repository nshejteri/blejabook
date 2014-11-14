# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='confirmation_key',
            field=models.CharField(default=b'', max_length=60),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='verified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
