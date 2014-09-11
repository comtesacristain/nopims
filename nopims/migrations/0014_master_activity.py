# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0013_auto_20140910_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='activity',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
