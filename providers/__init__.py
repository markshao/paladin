# define the base provider interface

class Provider(object):
    def create(self, **kwargs):
        raise NotImplemented

    def remove(self, node_id):
        raise NotImplemented

    @classmethod
    def provider_name(cls):
        return cls.name


from providers.docker import DockerProvider

PROVIDER_MAPPING = {
    DockerProvider.provider_name(): DockerProvider
}
