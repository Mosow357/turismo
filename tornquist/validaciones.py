from django.forms import ValidationError
from django.core.exceptions import ValidationError

def solo_caracteres(valor):
    if any(char.isdigit() for char in valor):
        raise ValidationError('el campo no puede ser numeros')

def clean_mensaje(data):
        
        if len(data) < 10:
            raise ValidationError('Debes especificar mejor el mensaje')
        return data

def valid_extension(value):
    if (not value.name.endswith('.png') and
        not value.name.endswith('.jpeg') and 
        not value.name.endswith('.gif') and
        not value.name.endswith('.bmp') and 
        not value.name.endswith('.jpg')):
 
        raise ValidationError("Archivos permitidos: .jpg, .jpeg, .png, .gif, .bmp")