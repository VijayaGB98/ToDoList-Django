from django.forms import ModelForm
from .models import *
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'priority', 'status')

        widgets = {
            'task_name': forms.TextInput(attrs={'class':'form-control mr-3 ml-3 my-3'}),
            'priority': forms.Select(attrs={'class':'form-control mr-3 ml-3 my-3'}),
            'status': forms.Select(attrs={'class':'form-control mr-3 ml-3 my-3'}),
        }