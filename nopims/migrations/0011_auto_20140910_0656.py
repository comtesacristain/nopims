# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nopims', '0010_auto_20140910_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('name', models.TextField()),
                ('master', models.OneToOneField(primary_key=True, serialize=False, to='nopims.Master')),
                ('well', models.ForeignKey(to='nopims.Well')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='explorationtitle',
            name='operator',
            field=models.ForeignKey(to='nopims.Operator'),
        ),
    ]
