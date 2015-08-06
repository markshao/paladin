from django.db import models

CLOUD_TYPE = (
    ("VMW", "vsphere"),
    ("DOCKER", "docker"),
    ("AWS", "amazon_ec2")
)

CLOUD_STATUS = (
    (0, "DISABLE"),
    (1, "ENABLE")
)


class CloudProviderType(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=CLOUD_TYPE)
    instances = models.IntegerField(default=0)

    def __unicode__(self):
        return self.type


class VsphereInstance(models.Model):
    provider = models.ForeignKey(CloudProviderType, related_name="vsphere_cloud_provider")
    ip = models.GenericIPAddressField(blank=True, null=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    vm_count = models.IntegerField()
    status = models.IntegerField(choices=CLOUD_STATUS, default=0)

    def __unicode__(self):
        return self.pk


class DockerInstance(models.Model):
    provider = models.ForeignKey(CloudProviderType, related_name="docker_cloud_provider")
    ip = models.GenericIPAddressField(blank=True,null=True,default=None)
    port = models.IntegerField(default=2376)
    tls_verify = models.BooleanField(default=True)
    cert_path = models.CharField(max_length=500)
    container_count = models.IntegerField()
    status = models.IntegerField(choices=CLOUD_STATUS, default=0)

    def __unicode__(self):
        return self.ip


ENV_STATUS = (
    (1, "READY"),
    (2, "DEPLOYING")
)


class Environment(models.Model):
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=ENV_STATUS, default=2)

    def __unicode__(self):
        return "env_%s" % self.name


class NodeType(models.Model):
    type_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.type_name


class Node(models.Model):
    node_name = models.CharField(max_length=255)
    node_type = models.ForeignKey(NodeType)
    env = models.ForeignKey(Environment, related_name="environment")
    ip = models.GenericIPAddressField(null=True, blank=True)
    splunkd_port = models.IntegerField(default=8000)
    splunkw_port = models.IntegerField(default=8089)
    ssh_port = models.IntegerField(default=22)
    splunk_username = models.CharField(max_length=30, default="admin")
    splunk_password = models.CharField(max_length=30, default="notchangeme")
    ssh_username = models.CharField(max_length=30, default="root")
    ssh_password = models.CharField(max_length=30, default="password")
    running = models.BooleanField(default=False)
    cloud_provider = models.ForeignKey(CloudProviderType, related_name="node_cloud_provider")
    provider_instance = models.IntegerField(blank=True, null=True)  # pk of instance table
    image_name = models.CharField(max_length=255, blank=True, null=True)
    container_id = models.CharField(max_length=255,blank=True, null=True)
    build_number = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return "%s_%s" % (self.node_name,self.node_type.type_name)

class ConnectionType(models.Model):
    type_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.type_name


class Connection(models.Model):
    source_node = models.ForeignKey(Node, related_name="source")
    target_node = models.ForeignKey(Node, related_name="target")
    connection_type = models.ForeignKey(ConnectionType, related_name="connection_type")
    env = models.ForeignKey(Environment, related_name="env")
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s_%s_connection" % (self.source_node.node_name,self.target_node.node_name)


from django.contrib import admin

admin.site.register(CloudProviderType)
admin.site.register(DockerInstance)
admin.site.register(VsphereInstance)
admin.site.register(Environment)
admin.site.register(NodeType)
admin.site.register(Node)
admin.site.register(ConnectionType)
admin.site.register(Connection)
