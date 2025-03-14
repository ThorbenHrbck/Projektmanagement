from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Projektmanagement.forms import TaskForm, UpdateTaskForm
from Projektmanagement.models import Task, Project, User


def main_view(request):
    return render(request, 'baseTemplate.html')


def project_overview(request):
    all_projects = Project.objects.all()
    paginator = Paginator(all_projects, 6)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    return render(request, 'Project/ProjectOverview.html', {'projects': projects})


def project_update(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == "POST":
        project.name = request.POST.get("ProjectName")
        project.start_date = request.POST.get("ProjectStartDate")
        project.end_date = request.POST.get("ProjectEndDate")
        project.notes = request.POST.get("ProjectDescription")
        try:
            user = User.objects.get(firstName=request.POST.get("ProjectOwner").split(" ")[0])
            project.owner = user
            project.save()
            return redirect('project_overview')
        except User.DoesNotExist:
            render(request, "error.html")
    return render(request, "Project/ProjectUpdate.html", {"project": project})


def project_create(request):
    return render(request, 'Project/ProjectCreate.html')


def project_create_submission(request):
    project_name = request.POST.get("ProjectName")
    project_start_date = request.POST.get("ProjectStartDate")
    project_end_date = request.POST.get("ProjectEndDate")
    project_owner_name = request.POST.get("ProjectOwner")
    project_description = request.POST.get("ProjectDescription")
    try:
        user = User.objects.get(firstName=project_owner_name)
        Project.objects.create(name=project_name, start_date=project_start_date, end_date=project_end_date,
                               notes=project_description, owner=user)
    except User.DoesNotExist:
        print("Unable")
    return project_create(request)


def project_delete(request):
    return render(request, 'Project/ProjectDelete.html')


def project_delete_new(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        project.delete()
        return redirect('project_overview')
    return render(request, 'Project/ProjectDelete.html', {'project': project})


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_overview', project_id=task.project.id)
    else:
        form = UpdateTaskForm(instance=task)

    return render(request, "Task/task_update.html", {"form": form, "task": task})


def task_overview(request, project_id):
    project = Project.objects.get(id=project_id)
    participants = User.objects.filter(project=project_id)

    all_tasks = Task.objects.filter(project=project_id).order_by('created_date')
    paginator = Paginator(all_tasks, 6)
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)
    return render(request, 'Task/task_overview.html',
                  {'tasks': tasks, 'project': project, 'participants': participants})


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
            return redirect('tasks_overview', project_id=task.project.id)
    else:
        form = TaskForm(initial={'project': project} if project else {})

    return render(request, "Task/task_create.html", {"form": form, "project": project})


def task_delete_page(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project = task.project
    return render(request, 'Task/task_delete.html', {'task': task, 'project': project})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project = task.project
    task.delete()
    return redirect('tasks_overview', project_id=project.id)


def toggle_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done
    task.save()
    return JsonResponse({'done': task.done})


def user_view(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return redirect('error')
    return user


def error(request):
    return render(request, 'error.html')
