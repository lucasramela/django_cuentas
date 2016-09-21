from django import forms
#from cuentas.models import Movimento


class SearchForm(forms.Form):
	query = forms.CharField(label='Busqueda',max_length=10)