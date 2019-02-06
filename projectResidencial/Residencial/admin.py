from django.contrib import admin

# Register your models here.
from Residencial.models import *


class AdminResidentes(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'edificio', 'no_apartamento',
					 'correo', 'telefono', 'cedula', 'clave']
	ordering = ['nombre','no_apartamento','edificio']

	list_filter = ('no_apartamento', 'edificio')
	search_fields = ('nombre',)

	class Meta:
		model = Residente

admin.site.register(Residente, AdminResidentes)


class AdminApartamento(admin.ModelAdmin):
	list_display = ['id', 'no_edificio', 'no_apartamento', 'propietario']

	class Meta:
		model = Apartamento

admin.site.register(Apartamento, AdminApartamento)


class AdminPagos(admin.ModelAdmin):
	list_display = ['id', 'fecha', 'propietario', 'no_edificio', 'pagos',
				'concepto', 'deuda_pendiente', 'recargo', 'concepto_deuda', 'estado']
	class Meta:
		model = Pago

admin.site.register(Pago, AdminPagos)



class AdminAjustes(admin.ModelAdmin):
	list_display = ['id', 'fecha_Para_Facturar', 'monto_Manteniento',
					'fecha_Limite_Pago', 'pago_Recargo']
	class Meta:
		model = Ajuste

admin.site.register(Ajuste, AdminAjustes)



class AdminEstado(admin.ModelAdmin):
	list_display = ['id', 'estado']
	class Meta:
		model = Estado

admin.site.register(Estado, AdminEstado)



class AdminSugerencias(admin.ModelAdmin):
	list_display = ['id', 'titulo', 'propietario', 'sugerencia', 'estado']
	class Meta:
		model = Sugerencia

admin.site.register(Sugerencia, AdminSugerencias)
