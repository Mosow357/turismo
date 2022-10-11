from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

# Create your views here.
def index(request):
    return render(request,'tornquist/publica/index.html')