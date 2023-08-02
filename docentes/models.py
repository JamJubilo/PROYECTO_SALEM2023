from django.db import models
from django.utils.translation import gettext_lazy as _

class Docentes(models.Model):
asignatura_imparte = models.CharField(max_length=45, verbose_name="Asignatura que imparte docente")
nombre_titulo = models.CharField(max_length=45,verbose_name="Titulo del docente")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")    
    

# Create your models here.
