from django.urls import path
from grados.views import grados

urlpatterns = [
    path('',grados, name="grados"),
]