from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Todo

# Add basic CRUD views (Create, Read, Update, Delete + Mark Complete)
def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})
