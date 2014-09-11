# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0007_auto_20140910_0431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explorationtitle',
            name='master',
        ),
        migrations.AddField(
            model_name='explorationtitle',
            name='operator',
            field=models.TextField(default='x'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='exploration_title',
            field=models.ForeignKey(to='nopims.ExplorationTitle', null=True),
            preserve_default=True,
        ),
    ]
