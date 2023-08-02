from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Usuarios(models.Model):
    nombres = models.CharField(max_length=50,verbose_name="nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellido usuario")
    num_documento = models.IntegerField(verbose_name="Numero documento del usuario")
    correo = models.CharField(max_length=45, verbose_name="correo usuario")
    direccion = models.CharField(max_length=45, verbose_name="Direccion usuario")
    num_telefono = models.IntegerField(verbose_name="numero telefónico del usuario")
    password = models.CharField(max_length=45, verbose_name="Password usuario")
    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        TI='T.I', _('Tarjeta de Identidad')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Empleado='Empleado', _('Empleado')
        Cliente='Cliente', _('Cliente')
        Proveedor='Proveedor', _('Proveedor')
    rol=models.CharField(max_length=13, choices=Rol.choices, default=Rol.Empleado, verbose_name="Rol")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")    
    
    def __str__(self) -> str:
        return "%s %s" %(self.nombre, self.apellido)
