
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render


from myapp.models import Project, Task
from django.shortcuts import render

# Create your views here.

def index(request):
    title = 'Wellcome'
    return render(request, "index.html", {'title': title})


def hello(request, name = None):
    return HttpResponse(f"<h1>Hello world, {name}</h1>")

def about(request):
    developer = 'Oscar T.'
    return render(request, 'about.html', {'developer': developer})

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def tasks(request, id):
    tasks = Task.objects.filter(project_id=id)
    
    return render(request, 'tasks.html', {'tasks': tasks})