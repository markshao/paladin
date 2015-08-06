# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpgraph', '0002_auto_20150805_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='build_number',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='node',
            name='image_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
