from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

# Create your views here.
def index(request):
    return render(request,'tornquist/publica/index.html')

def gastronomia(request):
    return render(request,'tornquist/publica/gastronomia.html')

def zonasAlojamientos(request):
    return render(request,'tornquist/publica/zonasAlojamientos.html')

def actividades(request):
    return render(request,'tornquist/publica/actividades.html')

def puntosInteres(request):
    return render(request,'tornquist/publica/puntosInteres.html')

def emergencias(request):
    return render(request,'tornquist/publica/emergencias.html')

def contacto(request):
    return render(request,'tornquist/publica/contacto.html')