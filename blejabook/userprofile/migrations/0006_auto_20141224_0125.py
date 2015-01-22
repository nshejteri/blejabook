# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20141223_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default=b'', upload_to=userprofile.models.generate_new_filename, null=True, verbose_name=b'profile image', blank=True),
        ),
    ]
