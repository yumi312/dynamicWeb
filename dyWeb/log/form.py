from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Log
from django.forms import ModelForm


class LogForm(ModelForm):
    class Meta:
        model = Log

        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contents': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # dropdowm list
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'edit_time': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': '名稱',       # labels['title']
            'description': '敘述',
            'slug': '代號',
            'category': '類別',
            'tags': '標籤',
        }
