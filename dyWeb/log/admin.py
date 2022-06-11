from django.contrib import admin
from .models import Author, Tag, Log
# Register your models here.

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Log)
