from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.


def index(request):
    return render(request, 'team/index.html',)


def project(request):
    return render(request, 'team/about_project.html',)


def contact(request):
    return render(request, 'team/contact_us.html',)
