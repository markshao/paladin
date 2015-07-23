# define the base provider interface

class Provider(object):
    def create(self, **kwargs):
        raise NotImplemented

    def remove(self, node_id):
        raise NotImplemented

    def provider_name(self):
        raise NotImplemented

