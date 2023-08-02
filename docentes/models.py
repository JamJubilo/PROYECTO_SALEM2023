from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuarios

class Docentes(models.Model):
    Usuario_id_usuario = models.ForeignKey(Usuarios,on_delete=models.PROTECT, verbose_name="usuario", related_name="usuario")
asignatura_imparte = models.CharField(max_length=45, verbose_name="Asignatura que imparte docente")

    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
    class Titulos(models.Model):
        Docente_id_Docente = models.ForeignKey(Docentes,on_delete=models.PROTECT,verbose_name="tiutlo del docente")  
        nombre_titulo = models.CharField(max_length=45,verbose_name="Titulo del docente")
        
    

# Create your models here.
