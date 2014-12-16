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
                ('subject', models.CharField(max_length=60, verbose_name='Subject')),
                ('body', models.TextField(verbose_name='Body')),
                ('sent_at', models.DateTimeField(null=True, verbose_name='sent at', blank=True)),
                ('read_at', models.DateTimeField(null=True, verbose_name='read at', blank=True)),
                ('replied_at', models.DateTimeField(null=True, verbose_name='replied at', blank=True)),
                ('sender_deleted_at', models.DateTimeField(null=True, verbose_name='Sender deleted at', blank=True)),
                ('recipient_deleted_at', models.DateTimeField(null=True, verbose_name='Recipient deleted at', blank=True)),
                ('parent_msg', models.OneToOneField(related_name=b'next_messages', null=True, blank=True, to='private_messages.Message', verbose_name='Parent message')),
                ('recipient', models.OneToOneField(related_name=b'received_messages', null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name=b'Recipient')),
                ('sender', models.OneToOneField(related_name=b'sent_messages', verbose_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
