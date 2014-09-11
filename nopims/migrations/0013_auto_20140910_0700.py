# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0012_auto_20140910_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='activity',
        ),
        migrations.AddField(
            model_name='master',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
