"""dyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from log import views as log_views
from team import views as team_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', team_views.index),
    # path('about/', team_views.about),
    path('contact/', team_views.contact),
    path('about_team/', team_views.abt_team),

    path('admin/', admin.site.urls),
    path('user/', user_views.index),
    path('log/', log_views.index),
    path('log/create/', log_views.create),
    path('log/edit/<int:pk>/', log_views.edit, name="edit"),
    path('log/delete/<int:pk>/', log_views.delete, name="delete"),

    path('detail/<slug:slug>/', log_views.detail),
    path('cates/<slug:slug>/', log_views.categories),
    path('tags/<slug:slug>/', log_views.tags),

    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
