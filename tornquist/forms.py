from django import forms
from django.forms import ValidationError

from .models import TipoConsulta, Consulta

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