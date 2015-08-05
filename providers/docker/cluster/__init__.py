from providers import Provider
from scheduler import ContainerCountScheduler

class DockerClusterProvider(Provider):
    def __init__(self):
        # TODO use the count based scheduler here
        self.scheduler = ContainerCountScheduler()

    def create(self, **kwargs):
        pass

    def remove(self, node_id):
        pass
