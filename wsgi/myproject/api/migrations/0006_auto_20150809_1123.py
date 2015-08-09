# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user_ddns_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ddns_update_time',
            field=models.IntegerField(default=0),
        ),
    ]
