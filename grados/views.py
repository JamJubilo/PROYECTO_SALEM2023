from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def grados(request):

    context={

    }
    return render(request,'grados/grados.html',context)

