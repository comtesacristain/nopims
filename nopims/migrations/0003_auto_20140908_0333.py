# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0002_auto_20140908_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
