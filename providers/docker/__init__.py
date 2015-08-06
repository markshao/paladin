from providers import Provider
from providers.docker.scheduler import ContainerCountScheduler
from providers.docker.docker_service import DockerService

class DockerProvider(Provider):
    name = "docker"

    def __init__(self):
        super(DockerProvider,self).__init__()
        self.scheduler = ContainerCountScheduler()

    def create(self, **kwargs):
        client, engine = self.scheduler.select_docker_engine()
        docker_service = DockerService(client)
        container = docker_service.start_container(**kwargs)
        return container,engine

    def remove(self, node_id):
        pass
