from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")