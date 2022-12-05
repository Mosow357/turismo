from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.views.generic import View
from tornquist.forms import ContactoForm
from tornquist.forms import SolicitudForm

from django.contrib import messages

from tornquist.models import Gastronomia, Actividades, PuntosInteres, ZonasAlojamientos, Consulta, TipoConsulta

from tornquist.forms import ContactoForm, RegistrarUsuarioForm

from django.contrib import messages


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'tornquist/publica/index.html')

def gastronomia(request):
    restaurantes = Gastronomia.objects.all
    return render(request,'tornquist/publica/gastronomia.html',{'restaurantes':restaurantes})

def zonasAlojamientos(request):
    alojamientos = ZonasAlojamientos.objects.all
    return render(request,'tornquist/publica/zonasAlojamientos.html',{'alojamientos':alojamientos})

def actividades(request):
    actividades = Actividades.objects.all
    return render(request,'tornquist/publica/actividades.html',{'actividades':actividades})

def puntosInteres(request):
    puntosInteres = PuntosInteres.objects.all
    return render(request,'tornquist/publica/puntosInteres.html',{'puntosInteres':puntosInteres})

def emergencias(request):
    return render(request,'tornquist/publica/emergencias.html')

# def contacto(request):
#     return render(request,'tornquist/publica/contacto.html')

class Contacto(FormView):
    template_name = 'tornquist/publica/contacto2.html'
    form_class = ContactoForm
    success_url = 'mensaje_enviado'

    def form_valid(self, form):
        form.save()
        #form.send_email()
        return super().form_valid(form)

class MensajeEnviado(View):
    template = 'tornquist/publica/mensaje_enviado.html'

    def get(self, request):
        params = {}
        params['nombre_sitio'] = 'Contacto'
        params['mensaje'] = 'mensaje de consulta realizada'
        return render(request, self.template, params)

class SolicitudView(FormView):
    template_name = 'tornquist/publica/solicitud.html'
    form_class = SolicitudForm
    success_url = 'mensaje_enviado'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)