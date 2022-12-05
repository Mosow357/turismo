from django.forms import ValidationError

def solo_caracteres(valor):
    if any(char.isdigit() for char in valor):
        raise ValidationError('el campo no puede ser numeros')

def clean_mensaje(data):
        
        if len(data) < 10:
            raise ValidationError('Debes especificar mejor el mensaje')
        return data