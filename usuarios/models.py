from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Usuarios(models.Model):
    nombres = models.CharField(max_length=50,verbose_name="nombre")
    apellidos = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=45)
    num_documento = models.IntegerField()
    correo = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    num_telefono = models.IntegerField()
    password = models.CharField(max_length=45)
    rol = models.CharField(max_length=45)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")    
    
    def __str__(self) -> str:
        return "%s %s" %(self.nombre, self.apellido)
