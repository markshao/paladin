import logging
import sys
from docker.errors import APIError
from providers.docker.docker_client import Client
from providers.docker.container import Container
from providers.docker.progress_stream import stream_output

logger = logging.getLogger("docker_service")

class DockerService(object):
    def __init__(self, cert_path=None, base_url=None, tls_verify=True):
        self.client = Client(cert_path=cert_path, base_url=base_url, tls_verify=tls_verify)

    def create_container(self, one_off=False, insecure_registry=False, **override_options):
        """
        Create a container for this service. If the image doesn't exist, attempt to pull
        it.
        """
        container_options = self._get_container_create_options(override_options, one_off=one_off)
        try:
            return Container.create(self.client, **container_options)
        except APIError as e:
            if e.response.status_code == 404 and e.explanation and 'No such image' in str(e.explanation):
                logger.info('Pulling image %s...' % container_options['image'])
                output = self.client.pull(
                    container_options['image'],
                    stream=True,
                    insecure_registry=insecure_registry
                )
                stream_output(output, sys.stdout)
                return Container.create(self.client, **container_options)
            raise