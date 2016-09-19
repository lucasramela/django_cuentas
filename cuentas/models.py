from django.db import models

# Create your models here.
from django.db import models
class Localidad(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Cuenta(models.Model):
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=500)
	localidad = models.ForeignKey(Localidad, default=1)
	email = models.EmailField()

	def __str__(self):
		return "{0}_{1}_{2}".format(self.nombre, self.localidad, self.email)

class Movimiento(models.Model):
	cuenta = models.ForeignKey(Cuenta)
	comprobante = models.TextField()
	fecha = models.DateField(auto_now=True)
	importe = models.DecimalField(max_digits=20, decimal_places=2, default=0)

	def __str__(self):
		return "{0} ({1})".format(self.importe, self.fecha)

class PerfilEmpleado(models.Model):
	fecha_ingreso = models.DateField()
	sueldo = models.DecimalField(max_digits=20, decimal_places=2,default=20000)

		
class GerenteDeCuentas(models.Model):
	nombre = models.CharField(max_length=300)
	cuentas = models.ManyToManyField(Cuenta)
	perfil = models.OneToOneField(PerfilEmpleado,null=True)

	def __str__(self):
		return self.nombre