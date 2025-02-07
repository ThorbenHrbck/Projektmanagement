from django.http import Http404
from django.shortcuts import render

from Projektmanagement.models import Task


def main_view(request):
    return render(request, 'baseTemplate.html')


def project_overview(request):
    return render(request, 'Project/ProjectOverview.html')


def project_create(request):
    return render(request, 'Project/ProjectCreate.html')


def task_detail(request, num):
    try:
        task = Task.objects.get(pk=num)
    except Task.DoesNotExist:
        raise Http404("Task not found")
    return render(request, 'task.html', {'task': task})


def task_overview(request):
    try:
        tasks = Task.objects.all()
    except Task.DoesNotExist:
        raise Http404("Tasklist empty")
    return render(request, 'task_list.html', {'tasks': tasks})
