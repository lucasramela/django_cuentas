from django import forms
from cuentas.models import Movimiento, Localidad


class SearchForm(forms.Form):
	query = forms.CharField(label='Busqueda',max_length=10)

	limit = forms.IntegerField(label='Limite', min_value=1, required=False)
	fecha = forms.DateField(label='Desde cuando', required=False)# ahí está el problema, en el form es datetime field y en el modelo es datefield

class MovimientoForm(forms.ModelForm):

	class Meta:
		model = Movimiento
		fields = ('cuenta', 'comprobante', 'importe')

# Formulario chiquito de localidades
class LocalidadForm(forms.ModelForm):

	 class Meta:
	 	model = Localidad
	 	fields = ('nombre',)

	 		