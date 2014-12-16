# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_text', models.TextField(verbose_name='Message_text')),
                ('sent_at', models.DateTimeField(null=True, verbose_name='Sent at', blank=True)),
                ('read_at', models.DateTimeField(null=True, verbose_name='Read at', blank=True)),
                ('replied_at', models.DateTimeField(null=True, verbose_name='Replied at', blank=True)),
                ('sender_deleted_at', models.DateTimeField(null=True, verbose_name='Sender deleted at', blank=True)),
                ('recipient_deleted_at', models.DateTimeField(null=True, verbose_name='Recipient deleted at', blank=True)),
                ('parent_msg', models.ForeignKey(related_name=b'next_messages', verbose_name='Parent message', blank=True, to='private_messages.Message', null=True)),
                ('recipient', models.ForeignKey(related_name=b'received_messages', verbose_name='Recipient', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sender', models.ForeignKey(related_name=b'sent_messages', verbose_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-sent_at',),
            },
            bases=(models.Model,),
        ),
    ]
