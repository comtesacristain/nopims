# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('release_date', models.DateField()),
                ('parent_category', models.TextField()),
                ('category', models.TextField()),
                ('activity_name', models.TextField()),
                ('title', models.TextField()),
                ('operator', models.TextField()),
                ('eno', models.IntegerField()),
                ('staff', models.TextField()),
                ('copied', models.TextField()),
                ('staged', models.TextField()),
                ('attached', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
