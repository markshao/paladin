from celery.task import task
from providers.docker import DockerProvider

provider = DockerProvider()

@task
def delay_create_container(image_name, node_id):
    provider.create(**{
        "image":"10.66.129.13:5000/coreqa/splunkbase",
        "ports":[8000,8089]
    })
    return "1"
