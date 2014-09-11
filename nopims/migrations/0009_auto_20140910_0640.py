# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0008_auto_20140910_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='exploration_title',
            field=models.ForeignKey(to='nopims.Well', null=True),
        ),
    ]
