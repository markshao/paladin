from celery.task import task
from providers.docker import DockerProvider
from dpgraph.models import Node

provider = DockerProvider()


@task
def delay_create_container(image_name, env_id, node_id, node_type):
    container_name = "%s-%s-%s" % (node_type, env_id, node_id)

    container,engine = provider.create(**{
        "image": image_name,
        "ports": ["8000", "8089", "22"],
        "name": container_name
    })

    # update the database
    ssh_port = container.ports["22/tcp"][0]["HostPort"]
    splunkd_port = container.ports["8089/tcp"][0]["HostPort"]
    splunkw_port = container.ports["8000/tcp"][0]["HostPort"]

    # update the db
    node = Node.objects.get(pk=int(node_id))
    node.ssh_port = ssh_port
    node.splunkd_port = splunkd_port
    node.splunkw_port = splunkw_port
    node.ip = engine.ip
    node.provider_instance = int(engine.pk)

    node.save()

