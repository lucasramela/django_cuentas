from django.db import models
from django.db.models import Q

# Create your models here.
class Localidad(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre


	@staticmethod
	def ultimos():
		return Localidad.objects.order_by('-id')[:15]

class Cuenta(models.Model):
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=500)
	localidad = models.ForeignKey(Localidad, default=1)
	email = models.EmailField()

	def __str__(self):
		return "{0}-{1}-{2}".format(self.nombre, self.localidad, self.email)


class Movimiento(models.Model):
	cuenta = models.ForeignKey(Cuenta)
	comprobante = models.TextField()
	fecha = models.DateField(auto_now=True)
	importe = models.DecimalField(max_digits=20, decimal_places=2, default=0)

	def __str__(self):
		return "{0} ({1})".format(self.importe, self.fecha)

	@staticmethod
	def get_with(query, limit, fecha):
		# hacemos la Q
		q1 = Q(cuenta__nombre__icontains=query)
		q2 = Q(comprobante__icontains=query)
		queryset = Movimiento.objects.filter(q1 | q2) 
		#retornamos los Q
		if (fecha):
			return Movimiento.objects.filter(q1 | q2).filter(fecha__gte=fecha)[:limit]
		else:
			return Movimiento.objects.filter(q1 | q2)[:limit]

	@staticmethod
	def ultimos():
		return Movimiento.objects.order_by('-fecha')[:10]


class PerfilEmpleado(models.Model):
	fecha_ingreso = models.DateField()
	sueldo = models.DecimalField(max_digits=20, decimal_places=2,default=20000)

		
class GerenteDeCuentas(models.Model):
	nombre = models.CharField(max_length=300)
	cuentas = models.ManyToManyField(Cuenta)
	perfil = models.OneToOneField(PerfilEmpleado,null=True)

	def __str__(self):
		return self.nombre

