from django import forms
#from cuentas.models import Movimento


class SearchForm(forms.Form):
	query = forms.CharField(label='Busqueda',max_length=10)

	limit = forms.IntegerField(label='Limite', min_value=1, required=False)
	fecha = forms.DateTimeField(label='Desde cuando', required=False)

# class MovimientoForm(forms.Form):
# 	class Meta:
# 		model = Movimento
# 		field = ('cuenta', 'comprobante', 'importe')