# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_messages', '0004_auto_20141213_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='message_text',
        ),
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
    ]
