from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404

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
            return project_overview(request)
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


def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task not found")
    return render(request, 'Task/TaskTemplate.html', {'task': task})


def task_overview(request, project_id):
    try:
        tasks = Task.objects.filter(project=project_id)
        project = Project.objects.get(pk=project_id)
        participants = User.objects.filter(project=project_id)
    except Task.DoesNotExist:
        raise Http404("Tasklist empty")
    return render(request, 'Task/TaskOverview.html', {'tasks': tasks, 'project': project})
