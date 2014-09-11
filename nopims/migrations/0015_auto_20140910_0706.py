# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0014_master_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='id',
        ),
        migrations.AlterField(
            model_name='master',
            name='activity',
            field=models.OneToOneField(primary_key=True, serialize=False, to='nopims.Activity'),
        ),
    ]
