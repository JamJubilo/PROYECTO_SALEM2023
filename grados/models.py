from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Estudiante

class Grado(models.Model):
    num_grado = models.CharField(max_length=2,verbose_name="Grado")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado") 
    
class Curso(models.Model):
    Grado_id_grado = models.ForeignKey(Grado,on_delete=models.CASCADE, null=True, blank=False, verbose_name="Grado", related_name="Grado")
    nombre_curso = models.CharField(max_length=20,verbose_name="Curso")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Matricula(models.Model):
    Estudiante_id_estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE, null=True, blank=False, verbose_name="Grado", related_name="Grado")
    curso_id_curso = models.ForeignKey(Curso,on_delete=models.CASCADE, null=True, blank=False, verbose_name="Grado", related_name="Grado")
    fecha = models.DateField(verbose_name="fecha de Matricula",help_text="DD/MM/AAAA")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado") 
