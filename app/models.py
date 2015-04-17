from django.db import models

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


"""
aqui creamos el usuario y super usuario para que ingresen con email y no con 
"""
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
    
        #Creates and saves a User with the given email, date of
        #birth and password.
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )


        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        
        user.save(using=self._db)
        return user


"""
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_responsable = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def create_user(self, email, password=None):
    
        #Creates and saves a User with the given email, date of
        #birth and password.
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
"""

# Create your models here.

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_responsable = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email



class Materia(models.Model):
	materia = models.CharField(max_length=70)
	def __str__(self):
		return  self.materia


class Grado(models.Model):
	grado = models.IntegerField()
	
	def __str__(self):
		return  "%s" % (self.grado)


class GradoMateria(models.Model):
	materia = models.ForeignKey(Materia)
	grado = models.ForeignKey(Grado)

	class Meta:
		unique_together = ('materia', 'grado')

	def __str__(self):
		return  str(self.grado)+" - "+str(self.materia) 
"""
class Persona(models.Model):
	TIPO_DOCUMENTO = (
		('C.C.','Cedula de Ciudadania'),
		('T.I.','Tarjeta de Identidad'),
		)
	SEXO=(
		('M','Masculino'),
		('F','Femenino'),
		)
	user = models.OneToOneField(MyUser)
	identificacion = models.IntegerField(primary_key=True)
	nombres = models.CharField("Nombres Completos",max_length=30)
	apellidos = models.CharField("Apellidos Completos",max_length=30)
	tipo_documento = models.CharField(max_length=15,choices=TIPO_DOCUMENTO)
	#email = models.EmailField(max_length=75)
	#password = models.CharField(max_length=140)
	telefono=  models.CharField(max_length=15)
	direccion = models.CharField("Direccion",max_length=100)
	sexo = models.CharField(max_length=1, choices=SEXO)
	def __unicode__(self):
		return self.nombres +" "+ self.apellidos
	def __str__(self):
		return  self.nombres +" "+ self.apellidos
"""
class Responsable(models.Model):
	TIPO_DOCUMENTO = (
		('C.C.','Cedula de Ciudadania'),
		('T.I.','Tarjeta de Identidad'),
		)
	SEXO=(
		('M','Masculino'),
		('F','Femenino'),
		)
	user = models.OneToOneField(MyUser)
	tipo_documento = models.CharField(max_length=15,choices=TIPO_DOCUMENTO)
	identificacion = models.IntegerField(primary_key=True)
	nombres = models.CharField("Nombres Completos",max_length=30)
	apellidos = models.CharField("Apellidos Completos",max_length=30)
	
	#email = models.EmailField(max_length=75)
	#password = models.CharField(max_length=140)
	telefono=  models.CharField(max_length=15)
	direccion = models.CharField("Direccion",max_length=100)
	sexo = models.CharField(max_length=1, choices=SEXO)
	def __unicode__(self):
		return self.nombres +" "+ self.apellidos
	def __str__(self):
		return  self.nombres +" "+ self.apellidos
	


class Estudiante(models.Model):
	
	TIPO_DOCUMENTO = (
		('C.C.','Cedula de Ciudadania'),
		('T.I.','Tarjeta de Identidad'),
		)
	SEXO=(
		('M','Masculino'),
		('F','Femenino'),
		)
	user = models.OneToOneField(MyUser)
	codigo = models.CharField(max_length=140)
	tipo_documento = models.CharField(max_length=15,choices=TIPO_DOCUMENTO)
	identificacion = models.IntegerField(primary_key=True)
	nombres = models.CharField("Nombres Completos",max_length=30)
	apellidos = models.CharField("Apellidos Completos",max_length=30)
	telefono=  models.CharField(max_length=15)
	direccion = models.CharField("Direccion",max_length=100)
	sexo = models.CharField(max_length=1, choices=SEXO)
	responsables = models.ManyToManyField(Responsable)
	
	def __str__(self):
		return  self.codigo


class Profesor(models.Model):

	TIPO_DOCUMENTO = (
		('C.C.','Cedula de Ciudadania'),
		('T.I.','Tarjeta de Identidad'),
		)
	SEXO=(
		('M','Masculino'),
		('F','Femenino'),
		)
	tipo_documento = models.CharField(max_length=15,choices=TIPO_DOCUMENTO)
	user = models.OneToOneField(MyUser)
	identificacion = models.IntegerField(primary_key=True)
	nombres = models.CharField("Nombres Completos",max_length=30)
	apellidos = models.CharField("Apellidos Completos",max_length=30)
	telefono=  models.CharField(max_length=15)
	direccion = models.CharField("Direccion",max_length=100)
	sexo = models.CharField(max_length=1, choices=SEXO)	
	imagen = models.ImageField(upload_to='perfilprofe/', blank=True, null = True)
	materias = models.ManyToManyField(GradoMateria)

	def __unicode__(self):
		return self.nombres +" "+ self.apellidos
	def __str__(self):
		return  self.nombres +" "+ self.apellidos
