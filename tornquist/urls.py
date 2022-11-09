from django.urls import path, re_path

from . import views

urlpatterns = [
    path('',views.index, name='inicio' ),
    path('gastronomia/',views.gastronomia,name='gastronomia'),
    path('zonasAlojamientos/',views.zonasAlojamientos,name='zonasAlojamientos'),
    path('actividades/',views.actividades,name='actividades'),
    path('puntosInteres/',views.puntosInteres,name='puntosInteres'),
    path('emergencias/',views.emergencias,name='emergencias'),
    path('contacto/',views.contacto,name='contacto'),
    
]