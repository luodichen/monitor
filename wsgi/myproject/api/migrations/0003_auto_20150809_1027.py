# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_dnspodaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNSPodDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.TextField()),
                ('domain_id', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='sub_domain',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sub_domain_id',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='domain',
            field=models.ForeignKey(to='api.DNSPodDomain', null=True),
        ),
    ]
