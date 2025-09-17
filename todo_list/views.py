from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from datetime import datetime

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    all_items = List.objects.all()
    return render(request, 'todo_list/home.html', {'all_items': all_items})

def about(request):
    return render(request, 'todo_list/about.html', {'myname': 'Bob'})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('home')

def strike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

