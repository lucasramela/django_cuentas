import datetime
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from cuentas.models import Cuenta, Movimiento, Localidad, PerfilEmpleado
from cuentas.forms import SearchForm, MovimientoForm, LocalidadForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
	return render(request, 'base.html', {})

@login_required
def fecha(request):
	now = datetime.datetime.now()
	html = "<html><body> Hoy es %s.</body></html>".format(now)
	html = "<html><body> El año es {0}.</body></html>".format(now.year)
	return HttpResponse(html)

@login_required
@permission_required('cuentas.ver_cuentas')
def cuentas(request):
	return render (request, 'cuentas2.html', {'cuentas':Cuenta.objects.all(), 'total': Cuenta.objects.count()})

@login_required
@permission_required('cuentas.ver_cuentas')
def cuenta(request, id):
	try:
		c = Cuenta.objects.get(pk=id)
		m = Cuenta.objects.get(pk=id).movimiento_set.all()
	except Cuenta.DoesNotExist:
		raise Http404("No existe la cuenta seleccionada")
	return render (request, 'cuenta2.html',{'cuenta' : c, 'movimientos': m})

@login_required
@permission_required('cuentas.ver_busqueda')
def busqueda(request):
	# preguntamos si se esta usando el metodo post
	if request.method == 'POST':
		# import ipdb; ipdb.set_trace()
		# generamos la instancia de fomrs
		form = SearchForm(request.POST)
		# preguntamos si son validos los datos
		if form.is_valid():
			# aca instanciamos el cleaned_data que devolvio valid
			query = form.cleaned_data['query']
			limit = form.cleaned_data['limit']
			fecha = form.cleaned_data['fecha']
			# aplicamos un metodo personal para realizar la busqueda que queremos
			movimientos = Movimiento.get_with(query, limit, fecha)
			# retornamos los resultados
			return render(request, 'resultado.html', {'query': query, 'movimientos': movimientos})
	else:
		form = SearchForm()
	return render(request, 'busqueda.html', {'form': form})

@login_required
@permission_required('cuentas.ver_movimientos')
def movimientos(request):
	if request.method == 'POST':
		form = MovimientoForm(request.POST)
		if form.is_valid():
			movimiento = form.save(commit=False)
			movimiento.save()
			return render(request, 'movimientos.html', {'movimientos': Movimiento.ultimos()})
	# si no es POST (es get)
	else:
		form = MovimientoForm()
		return render(request, 'get_movimientos.html', {'form': form, 'movimientos': Movimiento.ultimos()})

@login_required
def localidades(request):
	# 2 - y esto es si doy a guardar
	if request.method == 'POST':
		form = LocalidadForm(request.POST)
		if form.is_valid():

			localidad = form.save(commit=False)
			localidad.save()

			return render(request, 'localidades.html', {'localidades': Localidad.ultimos()}) 
	# 1 - esta es la vista
	else:
		form = LocalidadForm()
		return render(request, 'get_localidades.html', {'form': form, 'localidades': Localidad.ultimos()})

