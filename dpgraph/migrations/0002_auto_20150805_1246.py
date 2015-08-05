# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpgraph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='provider_instance',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
