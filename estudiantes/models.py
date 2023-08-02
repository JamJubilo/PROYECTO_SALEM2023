from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Estudiantes(models.Model):
    fecha_nacimiento = models.DateTimeField()
    factor_rh = models.CharField(max_length=20)
    num_telefono = models.IntegerField()
    nom_acudiente = models.CharField(max_length=50,verbose_name="nombre")
    telefono_acudiente = models.IntegerField()
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")    
    
    def __str__(self) -> str:
        return "%s %s" %(self.nombre, self.apellido)


# Create your models here.