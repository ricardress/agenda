from asyncio.windows_events import NULL
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm


def index(request, letter = NULL):
    if letter != NULL:
        contactos = Contacto.objects.filter(nombre__istartswith=letter)
    else:
        contactos = Contacto.objects.filter(nombre__contains=request.GET.get('buscar', ''))
        
    context = {
        'contactos': contactos
    }

    return render(request, 'contacto/index.html', context)


def view(request, id):
    contactos = Contacto.objects.get(id=id)

    context = {
        'contactos': contactos
    }

    return render(request, 'contacto/detail.html', context)



def edit(request, id):
    contactos = Contacto.objects.get(id=id)

    if request.method =="GET":
        form = ContactoForm(instance=contactos)
        context = {
            'form': form,
            'id': id 
        }
        return render(request, 'contacto/edit.html',context)
    
    if request.method=="POST":
        form = ContactoForm(request.POST, instance= contactos)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id 
        }
        messages.success(request, 'Contacto actualizado') 
        return render(request, 'contacto/edit.html',context)

def create(request):
    if request.method =="GET":
        form = ContactoForm()
        context = {
            'form': form
        }
        return render(request, 'contacto/create.html', context)
    
    if request.method =="POST":
        form = ContactoForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('contacto')
    
def delete(request,id):
    contactos = Contacto.objects.get(id=id)
    contactos.delete()
    return redirect('contacto')
        
