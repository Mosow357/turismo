from django import forms
from django.forms import ValidationError

from .models import TipoConsulta, Consulta, Solicitud

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields= ['nombre','telefono','email','asunto','mensaje']

    # tipo_consulta = (
    #     ('',' Seleccione'),
    #     (1,'Opcion 1'),
    #     (2,'Opcion 2'),
    #     (3,'Opcion 3'),
    # )
    
    nombre = forms.CharField(
            label='Nombre Completo',
            max_length=50,
            error_messages={
                'required':'Por favor completa el nombre'
            },
            # validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'name':'fullname','id':'name'})
        )
    
    telefono = forms.CharField(
            label = 'Numero de Telefono',
            error_messages={
                'required':'Por favor complete el numero telefonico',
                'errorlist':'Debe ingresar solo numeros'

            },
            # required=False,
            widget=forms.NumberInput(attrs={'type':'tel','name':'phone','id':'phone'})
    )
    email = forms.EmailField(
            label='Email',
            max_length=150,
            error_messages={
                'required':'Por favor completa el email'
            },
            required=False,
            widget=forms.TextInput(attrs={'type':'email','name':'email','id':'email'})
        )
    asunto = forms.ModelChoiceField(
        queryset= TipoConsulta.objects.all(),
        label='Asunto',
        # initial='0',
        error_messages={
                'required':'Seleccione un asunto'
            },
        # required=False,
        widget=forms.Select(attrs={'name':'affair','id':'affair'})
    )
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=500,
            required=False,
            widget=forms.Textarea(attrs={'name':'message','rows':3})
        )
   

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError('Debes especificar mejor el mensaje')
        return data

    # def clean_asunto(self):
    #     data = self.cleaned_data['asunto']
    #     return 'Asunto-'+data


class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' , 'password1', 'password2']

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
            'imagen':forms.FileInput()
        }        