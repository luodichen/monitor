# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_ddns_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ddns_update_time',
            field=models.IntegerField(null=True),
        ),
    ]
