# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0004_change'),
    ]

    operations = [
        migrations.RenameField(
            model_name='change',
            old_name='change',
            new_name='change_made',
        ),
        migrations.AlterField(
            model_name='change',
            name='date_recorded',
            field=models.DateTimeField(),
        ),
    ]
