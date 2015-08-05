import ssl
import logging
from docker import Client
from docker import tls
import os

logger = logging.getLogger("docker_client")


def docker_client(cert_path=None, base_url=None,tls_verify=True):
    """
    Returns a docker-py client configured using environment variables
    according to the same logic as the official Docker client.
    """

    if not cert_path:
        logger.warn("the cert_path is not send,use the local variable")
        cert_path = os.environ.get('DOCKER_CERT_PATH', '')

    if cert_path == '':
        logger.warn("local cert_path is empty, try anther .docker path")
        cert_path = os.path.join(os.environ.get('HOME', ''), '.docker')

    if not base_url:
        logger.warn("the base url is not send,use the local variable")
        base_url = os.environ.get('DOCKER_HOST')

    tls_config = None

    if tls_verify:
        parts = base_url.split('://', 1)
        base_url = '%s://%s' % ('https', parts[1])

        client_cert = (os.path.join(cert_path, 'cert.pem'), os.path.join(cert_path, 'key.pem'))
        ca_cert = os.path.join(cert_path, 'ca.pem')

        tls_config = tls.TLSConfig(
            ssl_version=ssl.PROTOCOL_TLSv1,
            verify=True,
            assert_hostname=False,
            client_cert=client_cert,
            ca_cert=ca_cert,
        )
    return Client(base_url=base_url, tls=tls_config)
