from django.shortcuts import render
from ..models import Project

def portfolio_view(request):
    projects = Project.objects.all()
    return render(request, 'base.html', {'projects': projects})
