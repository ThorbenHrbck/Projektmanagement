from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def main_view(request):
    return render(request, 'baseTemplate.html')

def project_overview(request):
    return render(request, 'Project/ProjectOverview.html')

def project_create(request):
    return render(request, 'Project/ProjectCreate.html')