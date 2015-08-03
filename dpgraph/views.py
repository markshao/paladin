from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from dpgraph.models import Environment
from dpgraph.serializers import EnvironmentSerializer


class JsonResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)

@csrf_exempt
def environment_list(request):

    # [GET]  return the environment list
    if request.method == "GET":
        enviroments = Environment.objects.all()
        serializer = EnvironmentSerializer(enviroments,many=True)
        return JsonResponse(serializer.data)

    # [POST] create the new environment
    elif request.method == "POST":
        pass

from django.conf.urls import url
urlpatterns = [
    url(r'^environments/$',environment_list),
]