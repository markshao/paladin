from rest_framework import serializers
from models import Environment, Node, Connection, CloudProviderType
from providers.docker.asynctasks import delay_create_container


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ("id", "name", "create_time")
        read_only_fields = ("id", "create_time")

    def create(self, validated_data):
        name = validated_data.pop("name")
        environment = Environment.objects.create(name=name)
        return environment


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ("id", "node_name", "node_type", "env", "ip", "splunkd_port",
                  "splunkw_port", "ssh_username", "ssh_password", "splunk_username", "splunk_password", "running",
                  "cloud_provider", "provider_instance", "image_name", "build_number")
        read_only_fields = (
            "id", "node_name", "env", "ip", "splunkd_port", "splunkw_port", "ssh_username", "ssh_password",
            "splunk_username",
            "splunk_password", "running", "provider_instance", "image_name", "build_number")

    def create(self, env_id, validated_data,request):
        node_type = validated_data.pop("node_type")
        cloud_provider = validated_data.pop("cloud_provider")
        env = Environment.objects.get(pk=int(env_id))
        node = None
        if cloud_provider.type == "DOCKER":
            image_name = request.POST["image_name"]
            node = Node.objects.create(env=env, node_type=node_type, cloud_provider=cloud_provider,
                                       image_name=image_name)
            delay_create_container.delay(image_name,env_id,node.pk,node_type.type_name)
        return node


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ("id", "source_node", "target_node", "connection_type", "create_time")
        read_only_fields = ("id", "create_time")

    def create(self, env_id, validated_data):
        source_node = validated_data.pop("source_node")
        target_node = validated_data.pop("target_node")
        connection_type = validated_data.pop("connection_type")

        env = Environment.objects.get(pk=int(env_id))

        if source_node.running and target_node.running:
            connection = Connection.objects.create(env=env, source_node=source_node, target_node=target_node,
                                                   connection_type=connection_type)
            return connection, True
        elif not source_node.running:
            return source_node, False
        elif not target_node.running:
            return target_node, False
