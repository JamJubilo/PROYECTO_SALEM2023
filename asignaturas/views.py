from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def asignaturas(request):

    context={

    }
    return render(request,'asignaturas/asignaturas.html',context)



