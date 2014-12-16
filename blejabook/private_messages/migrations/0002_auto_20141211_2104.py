# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('private_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='parent_msg',
            field=models.ForeignKey(related_name=b'next_messages', verbose_name='Parent message', blank=True, to='private_messages.Message', null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name=b'received_messages', verbose_name=b'Recipient', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name=b'sent_messages', verbose_name='Sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
