# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('private_messages', '0004_remove_message_replied_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedMessages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted_at', models.DateTimeField(verbose_name='deleted at')),
                ('deleted_by', models.ForeignKey(related_name=b'deleted_messages', verbose_name=b'deleted by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_text', models.TextField(verbose_name='message_text')),
                ('sent_at', models.DateTimeField(verbose_name='sent at', blank=True)),
                ('read_at', models.DateTimeField(null=True, verbose_name='read at', blank=True)),
                ('recipient', models.ForeignKey(related_name=b'received_messages', verbose_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name=b'sent_messages', verbose_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-sent_at',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name='created at')),
                ('participant_a', models.ForeignKey(related_name=b'participant_a', verbose_name=b'participant a', to=settings.AUTH_USER_MODEL)),
                ('participant_b', models.ForeignKey(related_name=b'participant_b', verbose_name=b'participant b', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='message',
            name='parent_msg',
        ),
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AlterUniqueTogether(
            name='thread',
            unique_together=set([('participant_a', 'participant_b')]),
        ),
        migrations.AddField(
            model_name='msg',
            name='thread',
            field=models.ForeignKey(related_name=b'thread_messages', verbose_name='thread', to='private_messages.Thread'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deletedmessages',
            name='id_of_last_del_msg',
            field=models.ForeignKey(verbose_name=b'ID of last deleted message', to='private_messages.Msg'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deletedmessages',
            name='thread',
            field=models.ForeignKey(verbose_name=b'thread ID of deleted messages', to='private_messages.Thread'),
            preserve_default=True,
        ),
    ]
