# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0003_auto_20140908_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('change', models.TextField()),
                ('date_recorded', models.DateField()),
                ('master', models.ForeignKey(to='nopims.Master')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
