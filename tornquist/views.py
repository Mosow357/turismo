from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader
from tornquist.models import Gastronomia, Actividades, PuntosInteres, ZonasAlojamientos
from tornquist.forms import ContactoForm
from django.contrib import messages

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

def contacto(request):
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST)
        if (contacto_form.is_valid()):
            #deberia agregar las acciones que necesito hacer
            
            contacto_form.save()
            messages.success(request,'Hemos recibido tu consulta, en breve te responderemos.')
            messages.info(request,'Te estará llegando un email.')
            contacto_form = ContactoForm()
        else:
            messages.warning(request,'Por favor revisa los errores del formulario.')

    else:
        contacto_form = ContactoForm()
        
    return render(request,'tornquist/publica/contacto2.html',{'contacto_form':contacto_form})