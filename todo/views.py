from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.filter(titulo__contains=request.GET.get('buscar', ''))
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)


def view(request, id):
    todos = Todo.objects.get(id=id)

    context = {
        'todos': todos
    }

    return render(request, 'todo/detail.html', context)

def edit(request, id):
    todos = Todo.objects.get(id=id)

    if request.method =="GET":
        form = TodoForm(instance=todos)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)

    if request.method=="POST":
        form = TodoForm(request.POST, instance=todos)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id
        }    
        messages.success(request, 'Tarea actualizada')
        return render(request, 'todo/edit.html', context)

def create(request):
    if request.method =="GET":
        form = TodoForm()
        context = {
            'form': form
        }
        return render(request, 'todo/create.html', context)

    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('todo')

def delete(request, id):
    todos = Todo.objects.get(id=id)
    todos.delete()
    return redirect('todo')

