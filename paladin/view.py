from django.shortcuts import render
from orchestration.asynctasks import a

def enviornment_list(request):
    rest = a.delay(1,2)
    print rest
    return render(request, "environ/environment_list.html")

def create_idx(request):
    if request.method == "GET":
        return render(request, "environ/create_cluster.html")