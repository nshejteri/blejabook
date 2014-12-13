# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('private_messages', '0002_auto_20141211_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name=b'received_messages', verbose_name=b'Recipient', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
