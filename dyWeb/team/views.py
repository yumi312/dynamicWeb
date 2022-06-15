from django.shortcuts import render
from django.http import HttpResponse

from log.models import Category, Tag
from . import models
# Create your views here.


def index(request):
    cates = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'team/index.html', {'cates': cates, 'tags': tags})


def about(request):
    return render(request, 'team/index.html',)


def contact(request):
    cates = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'team/contact_us.html', {'cates': cates, 'tags': tags})


def abt_team(request):
    cates = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'team/about_team.html', {'cates': cates, 'tags': tags})
