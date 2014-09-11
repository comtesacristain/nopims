# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0011_auto_20140910_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='master',
        ),
        migrations.RemoveField(
            model_name='master',
            name='id',
        ),
        migrations.RemoveField(
            model_name='master',
            name='well',
        ),
        migrations.AddField(
            model_name='activity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='activity',
            field=models.OneToOneField(primary_key=True, default=1, serialize=False, to='nopims.Activity'),
            preserve_default=False,
        ),
    ]
