from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect

from Projektmanagement.forms import TaskForm
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
        project = Project.objects.get(id=project_id)
        participants = User.objects.filter(project=project_id)

        all_tasks = Task.objects.filter(project=project_id).order_by('created_date')
        paginator = Paginator(all_tasks, 6)
        page_number = request.GET.get('page')
        tasks = paginator.get_page(page_number)
    except Task.DoesNotExist:
        raise Http404("Tasklist empty")
    return render(request, 'Task/TaskOverview.html', {'tasks': tasks, 'project': project, 'participants': participants})


def task_create(request, project_id=None):
    if project_id:
        project = Project.objects.get(id=project_id)
    else:
        project = None

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if project:
                task.project = project
            task.save()
            return redirect("project_overview")
    else:
        form = TaskForm(initial={'project': project} if project else {})

    return render(request, "Task/task_create.html", {"form": form, "project": project})


def task_delete(request, task_id=None):
    return render(request, 'Task/TaskDelete.html', {'task_id': task_id})


def toggle_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done
    task.save()
    return JsonResponse({'done': task.done})


def user_view(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("Could not find user")
    return user
