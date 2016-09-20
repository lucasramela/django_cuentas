import datetime
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from cuentas.models import Cuenta

# Create your views here.
def fecha(request):
	now = datetime.datetime.now()
#	html = "<html><body> Hoy es {0}.</body></html>".format(now)
	html = "<html><body> El año es {0}.</body></html>".format(now.year)
	return HttpResponse(html)

def cuentas (request):
	return render (request, 'cuentas2.html', {'cuentas':Cuenta.objects.all(), 'total': Cuenta.objects.count()})

def cuenta (request, id):
	try:
		c = Cuenta.objects.get(pk=id)
	except Cuenta.DoesNotExist:
		raise Http404("No existe la cuenta seleccionada")
	return render (request, 'cuenta2.html',{'cuenta' : c})