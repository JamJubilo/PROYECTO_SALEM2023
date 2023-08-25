from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from principal.views import inicio, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    
    path('asignaturas/',include('asignaturas.urls')),
    path('grados/',include('grados.urls')),
    path('usuarios/',include('usuarios.urls')),
    
    path('login/', auth_views.LoginView.as_view(), name='index-admin'),
    path('logout/', logout_user, name="logout")

    
]
