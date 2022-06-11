from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import user


def index(request):
    return render(request, 'login/index.html',)

# Create your views here.
