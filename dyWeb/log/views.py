from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .form import LogForm
from .models import Log

from django.contrib.auth.decorators import permission_required
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


def categories(request, slug=None):
    logs = Log.objects.filter(categories__slug=slug)
    return render(request, 'log/log_index.html', {'logs': logs})


@permission_required('log.add_log')
def create(request):
    if request.method == "POST":
        # 如果失敗 ->(request.POST, request.FILES)
        form = LogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = LogForm
    return render(request, "log/edit.html", {'form': form})
