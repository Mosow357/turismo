from django import forms
from django.forms import ValidationError

from .models import TipoConsulta, Consulta
from .models import Solicitud

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ['nombre', 'telefono', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre' : forms.TextInput(attrs={'name':"fullname", 'id':'name', 'required':'True'}),
            'telefono': forms.NumberInput(attrs={'name':"phone", 'id':'phone','type':'tel'}),
            'email' : forms.EmailInput(attrs={'name':"email", 'id':'email', 'type':'email', 'required':'True'}),
            'asunto' : forms.TextInput(attrs={'name':"affair", 'id':'affair', 'required':'True'}),
            'mensaje' : forms.Textarea(attrs={'name':"message", 'rows':'3'}),
        }
        
class SolicitudForm(forms.ModelForm):
    
    class Meta:
        RUBROS = [
        ("", "Seleccione un rubro"),
        (1, "Gastronomia"),
        (2, "Excurciones"),
        (3, "Entretenimiento"),
        ]
        UBICACIONES = [
            ("", "Seleccione una ubicacion"),
            (1, "Tornquist"),
            (2, "Sierra de la ventana"),
        ]
        
        model = Solicitud
        fields = ['nombre', 'ubicacion', 'rubro', 'direccion', 'telefono', 'sitio', 'imagen']
        widgets = {
            'nombre' : forms.TextInput(attrs={"placeholder": "Ingrese nombre del local/servicio",}),
            'ubicacion':forms.Select(choices=UBICACIONES),
            'rubro':forms.Select(choices=RUBROS),
            'direccion':forms.TextInput(attrs={"placeholder": "Ingrese la direccion del local"}),
            'telefono':forms.TextInput(),
            'sitio':forms.TextInput(attrs={"placeholder": "Ingrese el sitio web o link de su red social"}),
        }



class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' , 'password1', 'password2']