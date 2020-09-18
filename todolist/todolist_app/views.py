from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime

# Render homepage
def home(request):
    form = TaskForm()
    incomplete_tasks = Task.objects.filter(status='Incomplete')
    completed_tasks = Task.objects.filter(status='Complete')
    context = {'incomplete_tasks':incomplete_tasks, 'completed_tasks':completed_tasks, 'form':form}
    return render(request, 'todolist_app/tasklist.html', context)

def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return redirect('/')

def edit_or_delete_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        if request.POST.get('delete'):
            task.delete()
            return redirect('/')
        if request.POST.get('complete'):
            task.status = 'Complete'
            task.date_created = datetime.now()
            task.save()
            return redirect('/')
        if request.POST.get('update'):
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('/')
    context = {'task': task, 'form': form}
    return render(request, 'todolist_app/updatetask.html', context)