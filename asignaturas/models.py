from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Docente
from grados.models import Matricula
class Asignatura(models.Model):
    nombre_asignatura = models.CharField(max_length=45,verbose_name="Asignatura")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado") 
    
class DocenteAsignatura(models.Model):
    id_asignatura = models.ForeignKey(Asignatura,on_delete=models.PROTECT, verbose_name="Asignatura", related_name="Asignatura")
    id_docente = models.ForeignKey(Docente,on_delete=models.PROTECT, verbose_name="Asignatura", related_name="Asignatura")
    
class CursoAsignatura(models.Model):
    id_docenteAsignatura = models.ForeignKey(DocenteAsignatura, on_delete=models.PROTECT, verbose_name="Docente Asignatura", related_name="DocenteAsignatura")
    id_matricula = models.ForeignKey(Matricula, on_delete=models.PROTECT, verbose_name="Matricula", related_name="Matricula")
    
class Calificaciones(models.Model):
    id_cursoAsignatura = models.ForeignKey(CursoAsignatura, on_delete=models.PROTECT, verbose_name="Curso asignatura",related_name="CursoAsignatura")
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, verbose_name ="Calificación")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")  