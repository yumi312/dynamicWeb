from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .form import LogForm
from .models import Category, Log, Tag

from django.contrib.auth.decorators import permission_required
# Create your views here.


def index(request):
    q = request.GET.get('q', None)
    items = ""
    if q is None or q == "":
        logs = Log.objects.all()
        cates = Category.objects.all()
        tags = Tag.objects.all()
    elif q is not None:
        logs = Log.objects.filter(title__contains=q)
        cates = Category.objects.filter(title__contains=q)
        tags = Tag.objects.filter(title__contains=q)
    return render(request, 'log/log_index.html', {'logs': logs, 'cates': cates, 'tags': tags})

    # return render(request, 'log/log_index.html',)


def detail(request, slug=None):  # < here
    log = get_object_or_404(Log, slug=slug)
    cates = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'log/detail.html', {'log': log, 'cates': cates, 'tags': tags})

# def detail(request):  # < here
#     return render(request, 'log/detail.html')


def tags(request, slug=None):
    logs = Log.objects.filter(tags__slug=slug)
    cates = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'log/log_index.html', {'logs': logs, 'cates': cates, 'tags': tags})


def categories(request, slug=None):
    logs = Log.objects.filter(categories__slug=slug)
    cates = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'log/log_index.html', {'logs': logs, 'cates': cates, 'tags': tags})


@permission_required('log.add_log')
def create(request):
    if request.method == "POST":
        # 如果失敗 ->(request.POST, request.FILES)
        form = LogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/log")
    else:
        form = LogForm
    return render(request, "log/edit.html", {'form': form})


@permission_required('log.change_log')
def edit(request, pk=None):
    # 判斷物件存不存在，存在就傳回，不存在就404
    flower = get_object_or_404(Log, pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/log")
    else:
        form = LogForm(instance=flower)
    return render(request, "log/edit.html", {'form': form})


@permission_required('log.delete_log')
def delete(request, pk=None):
    log = get_object_or_404(Log, pk=pk)
    log.delete()
    return HttpResponseRedirect("/log")
