from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def project_overview(request):
    return render(request, 'Project/ProjectOverview.html')