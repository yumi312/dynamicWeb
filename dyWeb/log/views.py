from django.shortcuts import redirect, render
from django.http import HttpResponse

from . import models


def index(request):
    return render(request, 'log/index.html',)

# Create your views here.
