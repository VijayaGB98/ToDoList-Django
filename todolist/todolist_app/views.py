from django.shortcuts import render, redirect
from .models import *

# Render homepage
def home(request):
    incomplete_tasks = Task.objects.filter(status='Incomplete')
    completed_tasks = Task.objects.filter(status='Complete')
    context = {'incomplete_tasks':incomplete_tasks, 'completed_tasks':completed_tasks}
    return render(request, 'todolist_app/tasklist.html', context)
