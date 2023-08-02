from django.shortcuts import render

def hola_mundo(request):
    nombre = "Jamer"
    apellido= "Martinez Guerra"
    tel= "30004567895"
    context={
        "nombres": nombre,
        
        "apellidos": apellido,
        
        "telefono":tel
    }
    return render(request, "index.html", context)