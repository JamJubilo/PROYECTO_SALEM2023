from django.contrib import admin
from django.urls import path, include
from principal.views import hola_mundo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola_mundo, name="inicio"),
    path('asignaturas/',include('asignaturas.urls')),
    path('grados/',include('grados.urls')),
    path('usuarios/',include('usuarios.urls')),
    
]
