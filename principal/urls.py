from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from principal.views import inicio, index_admin, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('index-admin/',index_admin, name="index-admin"),
    
    path('asignaturas/',include('asignaturas.urls')),
    path('grados/',include('grados.urls')),
    path('usuarios/',include('usuarios.urls')),
    
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', logout_user, name="logout")

    
]
