from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from .models import Log
# Create your views here.


def index(request):
    q = request.GET.get('q', None)
    items = ""
    if q is None or q == "":
        logs = Log.objects.all()
    elif q is not None:
        logs = Log.objects.filter(title__contains=q)

    return render(request, 'log/log_index.html', {'logs': logs})

    # return render(request, 'log/log_index.html',)


def detail(request, slug=None):  # < here
    log = get_object_or_404(Log, slug=slug)
    return render(request, 'log/detail.html', {'log': log})

# def detail(request):  # < here
#     return render(request, 'log/detail.html')


def tags(request, slug=None):
    logs = Log.objects.filter(tags__slug=slug)
    return render(request, 'log/log_index.html', {'logs': logs})
