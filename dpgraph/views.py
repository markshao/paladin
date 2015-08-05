from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from dpgraph.models import Environment, Node, Connection
from dpgraph.serializers import EnvironmentSerializer, ConnectionSerializer, NodeSerializer
from providers.docker.asynctasks import delay_create_container


class JsonResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)


def response_schema(status_code, data, error_message=None):
    return JsonResponse({
        "statsu_code": status_code,
        "error_message": error_message,
        "data": data
    })

STATUS_CODE = {
    "SUCCESS":0
}

@csrf_exempt
def environment_list_view(request):
    if request.method == "GET":
        enviroments = Environment.objects.all()
        serializer = EnvironmentSerializer(enviroments, many=True)
        return response_schema(STATUS_CODE["SUCCESS"],serializer.data)

    elif request.method == "POST":
        serializer = EnvironmentSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        environment = serializer.create(serializer.validated_data)
        new_serializer = EnvironmentSerializer(environment)
        return response_schema(STATUS_CODE["SUCCESS"],new_serializer.data)


@csrf_exempt
def environment_nodes_view(request, env_id):
    if request.method == "GET":
        nodes = Node.objects.filter(env=env_id)
        serializer = NodeSerializer(nodes, many=True)
        return response_schema(STATUS_CODE["SUCCESS"],serializer.data)

    elif request.method == "POST":
        serializer = NodeSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        node = serializer.create(env_id, serializer.validated_data)
        new_serializer = NodeSerializer(node)
        task = delay_create_container.delay("1",node.pk)
        return response_schema(STATUS_CODE["SUCCESS"],new_serializer.data)


@csrf_exempt
def environment_node_view(request, env_id, node_id):
    if request.method == "GET":
        node = Node.objects.get(pk=int(node_id))
        serializer = NodeSerializer(node)
        return JsonResponse(serializer.data)


@csrf_exempt
def environment_connections_view(request, env_id):
    if request.method == "GET":
        connections = Connection.objects.filter(env=env_id)
        serializer = ConnectionSerializer(connections, many=True)
        return JsonResponse(serializer.data)

    elif request.method == "POST":
        serializer = ConnectionSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        connection, ok = serializer.create(env_id, serializer.validated_data)
        return JsonResponse([])


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
