# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_messages', '0003_auto_20141217_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='replied_at',
        ),
    ]
