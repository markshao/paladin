from django.shortcuts import render

def enviornment_list(request):
    return render(request,"env/environment_list.html")

def create_idx(request):
    if request.method == "GET":
        return render(request,"env/create_cluster.html")