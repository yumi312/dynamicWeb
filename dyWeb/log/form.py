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
            'title': forms.TextInput(attrs={'class': 'form-control mb-2 input-group'}),
            'author_name': forms.Select(attrs={'class': 'form-control  mb-2 input-group'}),
            'contents': forms.Textarea(attrs={'class': 'form-control mb-2 input-group'}),
            'slug': forms.TextInput(attrs={'class': 'form-control mb-2 input-group'}),
            # dropdowm list
            'tags': forms.SelectMultiple(attrs={'class': 'form-control mb-2 input-group'}),
            'categories': forms.Select(attrs={'class': 'form-control mb-2 input-group'}),
            'edit_time': forms.TextInput(attrs={'class': 'form-control mb-2 input-group', 'type': 'datetime-local'}),
        }
        labels = {
            'title': '名稱',
            'author_name': '作者',      # labels['title']
            'contents': '日誌',
            'slug': '代號',
            'category': '類別',
            'tags': '標籤',
            'edit_time': '編輯時間',
        }
