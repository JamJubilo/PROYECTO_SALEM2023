from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def usuarios(request):
    titulo = "Usuarios"
    context={
        'titulo': titulo
    }
    return render(request,'usuarios/usuarios.html',context)

def administrador(request):
    titulo = "Administrador"
    context={
        'titulo': titulo
    }
    return render(request,'usuarios/administrador.html',context)

