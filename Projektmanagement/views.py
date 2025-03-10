from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Projektmanagement.forms import TaskForm
from Projektmanagement.models import Task, Project, User


def main_view(request):
    return render(request, 'baseTemplate.html')


def project_overview(request):
    all_projects = Project.objects.all()
    paginator = Paginator(all_projects, 6)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    return render(request, 'Project/ProjectOverview.html', {'projects' : projects})


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
            print("Unable")
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
        Project.objects.create(name=project_name, start_date=project_start_date, end_date=project_end_date, notes=project_description, owner=user)
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


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_overview')
    else:
        form = TaskForm()

    return render(request, 'Task/task_create.html', {'form': form})


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
