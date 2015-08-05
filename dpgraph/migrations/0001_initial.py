# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloudProviderType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, choices=[(b'VMW', b'vsphere'), (b'DOCKER', b'docker'), (b'AWS', b'amazon_ec2')])),
                ('instances', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
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
            name='DockerInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('baseurl', models.CharField(max_length=255)),
                ('tls_verify', models.BooleanField(default=True)),
                ('cert_path', models.CharField(max_length=500)),
                ('container_count', models.IntegerField()),
                ('status', models.IntegerField(default=0, choices=[(0, b'DISABLE'), (1, b'ENABLE')])),
                ('provider', models.ForeignKey(related_name='docker_cloud_provider', to='dpgraph.CloudProviderType')),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=2, choices=[(1, b'READY'), (2, b'DEPLOYING')])),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_name', models.CharField(max_length=255)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
                ('splunkd_port', models.IntegerField(default=8000)),
                ('splunkw_port', models.IntegerField(default=8089)),
                ('splunk_username', models.CharField(default=b'admin', max_length=30)),
                ('splunk_password', models.CharField(default=b'notchangeme', max_length=30)),
                ('ssh_username', models.CharField(default=b'root', max_length=30)),
                ('ssh_password', models.CharField(default=b'password', max_length=30)),
                ('running', models.BooleanField(default=False)),
                ('provider_instance', models.IntegerField()),
                ('cloud_provider', models.ForeignKey(related_name='node_cloud_provider', to='dpgraph.CloudProviderType')),
                ('env', models.ForeignKey(related_name='environment', to='dpgraph.Environment')),
            ],
        ),
        migrations.CreateModel(
            name='NodeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VsphereInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('vm_count', models.IntegerField()),
                ('status', models.IntegerField(default=0, choices=[(0, b'DISABLE'), (1, b'ENABLE')])),
                ('provider', models.ForeignKey(related_name='vsphere_cloud_provider', to='dpgraph.CloudProviderType')),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='node_type',
            field=models.ForeignKey(to='dpgraph.NodeType'),
        ),
        migrations.AddField(
            model_name='connection',
            name='connection_type',
            field=models.ForeignKey(related_name='connection_type', to='dpgraph.ConnectionType'),
        ),
        migrations.AddField(
            model_name='connection',
            name='env',
            field=models.ForeignKey(related_name='env', to='dpgraph.Environment'),
        ),
        migrations.AddField(
            model_name='connection',
            name='source_node',
            field=models.ForeignKey(related_name='source', to='dpgraph.Node'),
        ),
        migrations.AddField(
            model_name='connection',
            name='target_node',
            field=models.ForeignKey(related_name='target', to='dpgraph.Node'),
        ),
    ]
