# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_name', models.CharField(max_length=255)),
                ('ip', models.GenericIPAddressField()),
                ('splunkd_port', models.IntegerField(default=8000)),
                ('splunkw_port', models.IntegerField(default=8089)),
                ('username', models.CharField(default=b'admin', max_length=30)),
                ('password', models.CharField(default=b'notchangeme', max_length=30)),
                ('env', models.ForeignKey(to='dpgraph.Environment')),
            ],
        ),
        migrations.CreateModel(
            name='NodeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='node_type',
            field=models.ForeignKey(to='dpgraph.NodeType'),
        ),
        migrations.AddField(
            model_name='conection',
            name='source_node',
            field=models.ForeignKey(related_name='source', to='dpgraph.Node'),
        ),
        migrations.AddField(
            model_name='conection',
            name='target_ndoe',
            field=models.ForeignKey(related_name='target', to='dpgraph.Node'),
        ),
    ]
