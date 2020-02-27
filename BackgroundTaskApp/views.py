from .tasks import do_task
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Go to /task page for running the task.')

def task_view(request):
    do_task(10)
    return HttpResponse('Task is completed.')