from django.shortcuts import redirect, render
from django.http import HttpResponse

from . import models
# Create your views here.


def index(request):
    return render(request, 'log/log_index.html',)
