from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from dpgraph.models import Environment,Node
from dpgraph.serializers import EnvironmentSerializer, ConnectionSerializer, NodeSerializer


class JsonResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)


@csrf_exempt
def environment_list_view(request):
    if request.method == "GET":
        enviroments = Environment.objects.all()
        serializer = EnvironmentSerializer(enviroments, many=True)
        return JsonResponse(serializer.data)


    elif request.method == "POST":
        serializer = EnvironmentSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return JsonResponse([])


@csrf_exempt
def environment_nodes_view(request, env_id):
    if request.method == "GET":
        nodes = Node.objects.filter(env = env_id)
        serializer = NodeSerializer(nodes, many=True)
        return JsonResponse(serializer.data)

    elif request.method == "POST":
        serializer = NodeSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.create(env_id,serializer.validated_data)
        return JsonResponse(["ok"])


@csrf_exempt
def environment_node_view(request, env_id, node_id):
    if request.method == "GET":
        pass


@csrf_exempt
def environment_connections_view(request, env_id):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass


@csrf_exempt
def environment_connection_view(request, env_id, connection_id):
    if request.method == "GET":
        pass


from django.conf.urls import url

urlpatterns = [
    url(r'^environments/$', environment_list_view),
    url(r'^environments/(?P<env_id>\d+)/nodes/$', environment_nodes_view),
    url(r'^environments/(?P<env_id>\d+)/nodes/(?P<node_id>\d+)$', environment_node_view),
    url(r'^environments/(?P<env_id>\d+)/connections/$', environment_connections_view),
    url(r'^environments/(?P<env_id>\d+)/connections/(?P<connection_id>\d+)/$', environment_connection_view)
]
