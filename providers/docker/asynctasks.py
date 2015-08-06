from celery.task import task
from providers.docker import DockerProvider

provider = DockerProvider()


@task
def delay_create_container(image_name, env_id, node_id, node_type):
    container_name = "%s_%s_%s" % (env_id, node_type, node_id)

    container = provider.create(**{
        "image": "markshao/rider_splunk:234",
        "ports": ["8000", "8089", "22"],
        "name":container_name
    })
