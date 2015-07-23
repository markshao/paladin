from django.db import models

class SplunkNodeType(models.Model):
    type_name = models.CharField(max_length=255)

class SplunkNode(models.Model):
    node_name = models.CharField(max_length=255)
    node_type = models.ForeignKey(SplunkNodeType)
    ip = models.IPAddressField()
    splunkd_port = models.IntegerField(max_length=5, default=8000)
    splunkw_port = models.IntegerField(max_length=5, default=8089)
    username = models.CharField(max_length=30, default="admin")
    password = models.CharField(max_length=30, default="notchangeme")


class RelationType(models.Model):
    pass

class Relation(models.Model):
    source_node = models.ForeignKey(SplunkNode)
    target_ndoe = models.ForeignKey(SplunkNode)




