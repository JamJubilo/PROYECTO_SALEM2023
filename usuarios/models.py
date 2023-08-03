from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Usuario(models.Model):
    nombres = models.CharField(max_length=50,verbose_name="nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellido usuario")
    direccion = models.CharField(max_length=45, verbose_name="Direccion usuario")
    num_telefono = models.CharField(max_length=45 ,verbose_name="numero telefónico del usuario")
    password = models.CharField(max_length=45, verbose_name="Password usuario")
    class TipoDocumento(models.IntegerChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        TI='T.I', _('Tarjeta de Identidad')
        PP='Pasaporte', _('pasaporte')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    num_documento = models.CharField(max_length=45,verbose_name="Numero documento del usuario")
    correo = models.CharField(max_length=45, verbose_name="correo usuario")

    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Estudiante='Estudiante', _('Estudiante')
        Docente='Docente', _('Docente')
    rol=models.CharField(max_length=13, choices=Rol.choices, default=Rol.Administrador, verbose_name="Rol")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado") 
    def __str__(self):
        return "%s %s" %(self.nombres, self.apellidos)  
class Estudiante(models.Model):
    Usuario_id_usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT, verbose_name="Usuario", related_name="Usuario")
    fecha_nacimiento = models.DateTimeField(verbose_name="fecha nacimiento del estudiante",help_text="DD/MM/AAAA")
    factor_rh = models.CharField(max_length=20, verbose_name="Factor RH estudiante")
    num_telefono = models.CharField(max_length=45,verbose_name="Numero de telfono del estudiante")
    nom_acudiente = models.CharField(max_length=50,verbose_name="nombre acudiente de estudiante")
    telefono_acudiente = models.CharField(max_length=45,verbose_name="Numero de telefono del acudiente") 
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")  
    
class Docente(models.Model):
    Usuario_id_usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT, verbose_name="usuario", related_name="usuario")
    asignatura_imparte = models.CharField(max_length=45, verbose_name="Asignatura que imparte docente")

    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo') 
        INACTIVO= '0', _('Inactivo') 
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
class Titulos(models.Model):
    Docente_id_Docente = models.ForeignKey(Docente,on_delete=models.PROTECT,verbose_name="tiutlo del docente")  
    nombre_titulo = models.CharField(max_length=45,verbose_name="Titulo del docente")
