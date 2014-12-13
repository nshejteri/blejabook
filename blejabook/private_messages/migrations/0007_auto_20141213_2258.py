# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_messages', '0006_auto_20141213_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.TextField(verbose_name='Message_asd'),
        ),
    ]
