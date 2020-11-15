from django.shortcuts import render
from .models import Project

def index(request, *args, **kwargs):
    projects = Project.objects.all()
    context = { 'projects': projects }
    return render(request, 'projects/index.html', context)

def details(request, *args, **kwargs):
    project_id = kwargs['id']
    project = Project.objects.get(pk=project_id)
    context = { 'project': project }
    return render(request, 'projects/details.html', context)

