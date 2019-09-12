from django.shortcuts import render
from webpersonal.portfolio.models import Project


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
