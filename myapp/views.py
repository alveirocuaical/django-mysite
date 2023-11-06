
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404


from myapp.models import Project, Task

# Create your views here.

def index(request):
    return HttpResponse("<h1> Index page </h1>")


def hello(request, name = None):
    return HttpResponse(f"<h1>Hello world, {name}</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    
    return HttpResponse(f"task : {task.title}")