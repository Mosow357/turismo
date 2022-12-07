from django.contrib import admin
from tornquist.models import Gastronomia, Actividades, PuntosInteres, ZonasAlojamientos
from tornquist.models import Consulta, Solicitud, RespuestaSolicitud, Respuesta
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
    list_display = ('nombre','telefono','pagina_web', 'estado_de_respuesta')
    list_editable= ('telefono','pagina_web')
    search_fields = ['nombre',]
    list_filter = ['estado']

class ActividadesMAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','pagina_web', 'estado_de_respuesta')
    list_editable= ('telefono','pagina_web')
    search_fields = ['nombre',]
    list_filter = ['estado']

class ZonasAlojamientoMAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','pagina_web', 'estado_de_respuesta')
    list_editable= ('telefono','pagina_web')
    search_fields = ['nombre',]
    list_filter = ['estado']

class PuntosInteresMAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','pagina_web', 'estado_de_respuesta')
    list_editable= ('telefono','pagina_web')
    search_fields = ['nombre',]
    list_filter = ['estado']

class RespuestaInLine(admin.TabularInline):
    model = Respuesta
    extra = 0

class ConsultaMAdmin(admin.ModelAdmin):
    inlines = [RespuestaInLine]

    list_display = [
        'nombre',
        'asunto',
        'estado_de_respuesta',
        'fecha',
    ]
    list_filter = ['estado_respuesta', 'fecha']

class RespuestaSolicitudInLine(admin.TabularInline):
    model = RespuestaSolicitud
    extra = 0

class SolicitudAdmin(admin.ModelAdmin):
    inlines = [RespuestaSolicitudInLine]

    list_display = [
        'nombre',
        'sitio',
        'rubro',
        'estado_de_respuesta',
        'fecha',
    ]

    list_filter = ['estado_respuesta', 'fecha']

mi_admin = TornquistAdminSite(name='tornquistadmin')
mi_admin.register(Gastronomia, GastronomiaMAdmin)
mi_admin.register(Actividades, ActividadesMAdmin)
mi_admin.register(ZonasAlojamientos, ZonasAlojamientoMAdmin)
mi_admin.register(PuntosInteres, PuntosInteresMAdmin)
mi_admin.register(Consulta, ConsultaMAdmin)
mi_admin.register(Solicitud, SolicitudAdmin)