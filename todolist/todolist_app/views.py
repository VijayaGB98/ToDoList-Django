from django.shortcuts import render, redirect
from .models import *

# Render homepage
def home(request):
    return render(request, 'todolist_app/main.html')
