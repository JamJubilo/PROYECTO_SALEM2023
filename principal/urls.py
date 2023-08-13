from django.contrib import admin
from django.urls import path, include
from principal.views import inicio, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('asignaturas/',include('asignaturas.urls')),
    path('grados/',include('grados.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('login/', login, name="login"),
]
