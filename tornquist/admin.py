from django.contrib import admin
from tornquist.models import Gastronomia, Actividades, PuntosInteres, ZonasAlojamientos, Consulta

from django.contrib.auth.models import User,Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Register your models here.

class TornquistAdminSite(admin.AdminSite):
    site_header = 'Administracion Turismo Tornquist'
    site_title = 'Administracion superusuario'
    index_title = 'Inicio de administración'
    empty_value_display = 'No hay datos para visualizar'


# admin.site.register(Gastronomia)
# admin.site.register(Actividades)
# admin.site.register(PuntosInteres)
# admin.site.register(ZonasAlojamientos)

class GastronomiaMAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','pagina_web')
    list_editable= ('telefono','pagina_web')
    search_fields = ['nombre',]

class ActividadesMAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','pagina_web')
    list_editable= ('telefono','pagina_web')
    search_fields = ['nombre',]

class ZonasAlojamientoMAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','pagina_web')
    list_editable= ('telefono','pagina_web')
    search_fields = ['nombre',]

class PuntosInteresMAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','pagina_web')
    list_editable= ('telefono','pagina_web')
    search_fields = ['nombre',]

class ConsultaMAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','mensaje')

mi_admin = TornquistAdminSite(name='tornquistadmin')
mi_admin.register(Gastronomia, GastronomiaMAdmin)
mi_admin.register(Actividades, ActividadesMAdmin)
mi_admin.register(ZonasAlojamientos, ZonasAlojamientoMAdmin)
mi_admin.register(PuntosInteres, PuntosInteresMAdmin)
mi_admin.register(Consulta, ConsultaMAdmin)
