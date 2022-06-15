from django.contrib import admin
from .models import Author, Tag, Log, Category
# Register your models here.

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Log)
admin.site.register(Category)
