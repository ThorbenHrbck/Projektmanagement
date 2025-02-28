from django.http import Http404, JsonResponse
from django.shortcuts import render

from Projektmanagement.models import Task, Project, User


def main_view(request):
    return render(request, 'baseTemplate.html')


def project_overview(request):
    return render(request, 'Project/ProjectOverview.html')


def project_update(request):
    return render(request, 'Project/ProjectUpdate.html')


def project_create(request):
    return render(request, 'Project/ProjectCreate.html')


def project_delete(request):
    return render(request, 'Project/ProjectDelete.html')


def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task not found")
    return render(request, 'Task/TaskTemplate.html', {'task': task})


def task_overview(request, project_id):
    try:
        tasks = Task.objects.filter(project=project_id)
        project = Project.objects.get(id=project_id)
        participants = User.objects.filter(project=project_id)
    except Task.DoesNotExist:
        raise Http404("Tasklist empty")
    return render(request, 'Task/TaskOverview.html', {'tasks': tasks, 'project': project, 'participants': participants})


def toggle_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done
    task.save()
    return JsonResponse({'done': task.done})


def user_view(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("Couldnt find user")
    return user
