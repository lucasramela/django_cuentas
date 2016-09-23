import datetime
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from cuentas.models import Cuenta, Movimiento
from cuentas.forms import SearchForm


# Create your views here.
def fecha(request):
	now = datetime.datetime.now()
	html = "<html><body> Hoy es {0}.</body></html>".format(now)
	html = "<html><body> El año es {0}.</body></html>".format(now.year)
	return HttpResponse(html)

def cuentas(request):
	return render (request, 'cuentas2.html', {'cuentas':Cuenta.objects.all(), 'total': Cuenta.objects.count()})

def cuenta(request, id):
	try:
		c = Cuenta.objects.get(pk=id)
		m = Cuenta.objects.get(pk=id).movimiento_set.all()
	except Cuenta.DoesNotExist:
		raise Http404("No existe la cuenta seleccionada")
	return render (request, 'cuenta2.html',{'cuenta' : c, 'movimientos': m})

def busqueda(request):
	# preguntamos si se esta usando el metodo post
	if request.method == 'POST':
		# generamos la instancia de fomrs
		form = SearchForm(request.POST)
		# preguntamos si son validos los datos
		if form.is_valid():
			# aca instanciamos el cleaned_data que devolvio valid
			query = form.cleaned_data['query']
			# aplicamos un metodo personal para realizar la busqueda que queremos
			movimientos = Movimiento.get_with(query)
			# retornamos los resultados
			return render(request, 'resultado.html', {'query': query, 'movimientos': movimientos})
	else:
		form = SearchForm()
	return render(request, 'busqueda.html', {'form': form})

