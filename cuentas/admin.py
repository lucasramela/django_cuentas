from django.contrib import admin
from cuentas import models

# Register your models here.
def set_zero(ModelAdmin, request, queryset):
	queryset.update(importe=0)
	set_zero.short_description="Convertir importe a Cero"

class  MovimientoAdmin(admin.ModelAdmin):
	date_hierarchy = 'fecha'
	list_filter =('cuenta__nombre',)
	list_display = ('importe','cuenta')
	actions = [set_zero]

class CuentaAdmin (admin.ModelAdmin):
	list_filter = ('localidad','nombre')

class LocalidadAdmin(admin.ModelAdmin):
	pass
	ordering = ('nombre',)


admin.site.register(models.Localidad, LocalidadAdmin)
admin.site.register(models.Cuenta, CuentaAdmin)
admin.site.register(models.Movimiento,MovimientoAdmin)
admin.site.register(models.GerenteDeCuentas)