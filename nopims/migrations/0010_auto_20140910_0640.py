# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0009_auto_20140910_0640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='master',
            old_name='exploration_title',
            new_name='well',
        ),
    ]
