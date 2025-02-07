from django.http import Http404
from django.shortcuts import render, get_object_or_404

from Projektmanagement.models import Task

def main_view(request):
    return render(request, 'baseTemplate.html')

def project_overview(request):
    return render(request, 'Project/ProjectOverview.html')

def project_create(request):
    return render(request, 'Project/ProjectCreate.html')

def get_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task not found")
    return render(request, 'task.html', {'task': task})


def task_list(request):
    try:
        tasks = Task.objects.all()
    except Task.DoesNotExist:
        raise Http404("Tasklist empty")
    return render(request, 'task_list.html', {'tasks': tasks})

def home(request):
    return None

def project(request):
    return None

