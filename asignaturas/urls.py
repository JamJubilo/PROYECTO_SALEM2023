from django.urls import path
from asignaturas.views import asignaturas

urlpatterns = [
    path('',asignaturas, name="asignaturas"),
]
