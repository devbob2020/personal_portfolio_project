from django.shortcuts import render
from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects':projects})

def blog(request):
    return render(request, 'portfolio/blog.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
