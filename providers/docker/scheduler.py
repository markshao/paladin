from dpgraph.models import DockerInstance
from providers.docker.docker_client import docker_client
import logging

logger = logging.getLogger("docker_scheduler")


class Scheduler(object):
    def select_docker_engine(self):
        raise NotImplemented


class ContainerCountScheduler(Scheduler):
    def select_docker_engine(self):
        docker_engines = DockerInstance.objects.filter(status=1)
        if len(docker_engines) == 0:
            logger.warn("no available docker engines for use")
            return None
        else:
            docker_engines = list(docker_engines)
            docker_engines.sort(lambda x, y: x.container_count - y.container_count)
            engine = docker_engines[0]
            base_url = "tcp://%s:%s" % (engine.ip, engine.port)
            return docker_client(cert_path=engine.cert_path, base_url=base_url,
                                 tls_verify=bool(engine.tls_verify)), engine
