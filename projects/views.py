from django.shortcuts import render
from .models import Project
# Create your views here.

def project_index_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects_index.html', context)

def project_details_view(request, id):
    project = Project.objects.get(id = id)
    context = {
        'project': project
    }
    return render(request, 'project_details.html', context)