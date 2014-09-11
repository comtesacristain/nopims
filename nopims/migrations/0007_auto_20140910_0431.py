# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0006_explorationtitle_path_status_well'),
    ]

    operations = [
        migrations.RenameField(
            model_name='change',
            old_name='change_made',
            new_name='attribute',
        ),
        migrations.AddField(
            model_name='change',
            name='new_value',
            field=models.TextField(default=datetime.date(2014, 9, 10)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='change',
            name='old_value',
            field=models.TextField(default=datetime.date(2014, 9, 10)),
            preserve_default=False,
        ),
    ]
