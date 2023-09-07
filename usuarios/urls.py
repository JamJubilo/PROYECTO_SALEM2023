from django.urls import path
from usuarios.views import administrador, usuarios

urlpatterns = [
    path('',usuarios, name="usuarios"),
    path('administrador/',administrador,name="administrador")
]