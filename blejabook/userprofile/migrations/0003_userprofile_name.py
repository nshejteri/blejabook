# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20141117_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=b'', max_length=40, verbose_name=b'First-Last Name'),
            preserve_default=True,
        ),
    ]
