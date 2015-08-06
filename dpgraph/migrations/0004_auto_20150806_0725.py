# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpgraph', '0003_auto_20150806_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dockerinstance',
            name='baseurl',
        ),
        migrations.AddField(
            model_name='dockerinstance',
            name='ip',
            field=models.GenericIPAddressField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dockerinstance',
            name='port',
            field=models.IntegerField(default=2376),
        ),
        migrations.AddField(
            model_name='node',
            name='container_id',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='node',
            name='ssh_port',
            field=models.IntegerField(default=22),
        ),
    ]
