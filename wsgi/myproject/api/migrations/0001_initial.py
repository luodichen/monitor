# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('token', models.TextField()),
                ('creat_time', models.IntegerField()),
                ('last_active_time', models.IntegerField(default=0)),
                ('last_active_ip', models.TextField(null=True)),
            ],
        ),
    ]
