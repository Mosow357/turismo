from django.urls import path, re_path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='inicio' ),
    path('gastronomia/',views.gastronomia,name='gastronomia'),
    path('zonasAlojamientos/',views.zonasAlojamientos,name='zonasAlojamientos'),
    path('actividades/',views.actividades,name='actividades'),
    path('puntosInteres/',views.puntosInteres,name='puntosInteres'),
    path('emergencias/',views.emergencias,name='emergencias'),
    path('contacto/',views.contacto,name='contacto'),

    # path('editar/<int:id_consulta>',views.EditarContacto,name='editar'),

    path('cuentas/registrarse', views.registrarse,name='registrarse'),
    # path('cuentas/login/',views.login,name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='tornquist/publica/login.html'), name='login'),  
    # path('cuentas/logout/', auth_views.LogoutView.as_view(template_name='tornquist/publica/index.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('solicitud/', views.SolicitudView.as_view(), name='solicitud'),
    # path('solicitud/mensaje_enviado/', views.MensajeEnviado.as_view(), name='mensaje_enviado'),
    # path('solicitud/',views.solicitud,name='solicitud'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)