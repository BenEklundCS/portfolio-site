from django.shortcuts import render
#from ..models import Project

def portfolio_view(request):
    #projects = Project.objects.all()
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def projects_view(request):
    return render(request, 'projects.html')

def skills_view(request):
    return render(request, 'skills.html')

def contact_view(request):
    return render(request, 'contact.html')
