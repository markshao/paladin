from django.db import models


class Environment(models.Model):
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now=True)


class NodeType(models.Model):
    type_name = models.CharField(max_length=255)


class Node(models.Model):
    node_name = models.CharField(max_length=255)
    node_type = models.ForeignKey(NodeType)
    env = models.ForeignKey(Environment)
    ip = models.GenericIPAddressField()
    splunkd_port = models.IntegerField(default=8000)
    splunkw_port = models.IntegerField(default=8089)
    username = models.CharField(max_length=30, default="admin")
    password = models.CharField(max_length=30, default="notchangeme")


class ConnectionType(models.Model):
    type_name = models.CharField(max_length=30)


class Conection(models.Model):
    source_node = models.ForeignKey(Node, related_name="source")
    target_ndoe = models.ForeignKey(Node, related_name="target")
    create_time = models.DateTimeField(auto_now=True)
