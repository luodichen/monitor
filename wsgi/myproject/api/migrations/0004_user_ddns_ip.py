# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150809_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ddns_ip',
            field=models.TextField(null=True),
        ),
    ]
