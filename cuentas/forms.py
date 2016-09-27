from django import forms
from cuentas.models import Movimiento


class SearchForm(forms.Form):
	query = forms.CharField(label='Busqueda',max_length=10)

	limit = forms.IntegerField(label='Limite', min_value=1, required=False)
	fecha = forms.DateTimeField(label='Desde cuando', required=False)

class MovimientoForm(forms.ModelForm):

	class Meta:
		model = Movimiento
		fields = ('cuenta', 'comprobante', 'importe')