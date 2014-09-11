# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0015_auto_20140910_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='well',
            field=models.ForeignKey(to='nopims.Well', null=True),
        ),
    ]
