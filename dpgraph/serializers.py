from rest_framework import serializers
from models import Environment, Node, Connection


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ("id", "name")
        read_only_fields = ("create_time")

    def create(self, validated_data):
        name = validated_data.pop("name")
        environment = Environment.objects.create(name=name)
        return environment


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ("node_name", "node_type", "env")
        read_only_fields = ("ip", "splunkd_port", "splunkw_port", "username", "password", "running")

    def create(self, env_id, validated_data):
        node_name = validated_data.pop("node_name")
        node_type = validated_data.pop("node_type")
        env = Environment.objects.get(pk=int(env_id))
        node = Node.objects.create(node_name=node_name,env=env,node_type=node_type)
        return node


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ("source_node", "target_node")
        read_only_fields = ("create_time")

    def create(self, validated_data):
        node_name = validated_data.pop("node_name")
        node_type = validated_data.pop("node_type")
        env = validated_data.pop("env")
