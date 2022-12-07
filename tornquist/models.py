from django.db import models
from datetime import datetime
from django.utils.html import format_html
from tornquist.validaciones import solo_caracteres, clean_mensaje, valid_extension
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from django.shortcuts import render

from django.template.loader import get_template
import threading

# Create your models here.

def create_mail(user_mail, subject, template_name, context):
    template = get_template(template_name)
    content = template.render(context)

    message = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[
            user_mail
        ],
    )

    message.attach_alternative(content, 'text/html')
    return message


def carpetas_de_guardado(instance, filename):
    return os.path.join(str(instance.rubro), filename)

class CardABS(models.Model):

    ACEPTADA    = 'Aceptada'
    BAJA        = 'Baja'

    ESTADOS = (
        (ACEPTADA, 'Aceptada'),
        (BAJA , 'Baja'),
    )

    nombre = models.CharField(max_length=100,verbose_name='nombre')
    ubicacion = models.CharField(max_length=150,verbose_name='ubicacion')
    telefono = models.CharField(max_length=150,verbose_name='telefono')
    direccion = models.CharField(max_length=150,verbose_name='direccion')
    pagina_web = models.CharField(max_length=150,verbose_name='pagina_web')
    estado = models.CharField(max_length=15, choices=ESTADOS, default=ACEPTADA)

    class Meta:
        abstract = True

    def estado_de_respuesta(self,):
        if self.estado == 'Aceptada':
            return format_html('<span style="background-color:#0a0; color:#fff;padding:5px;">{}</span>', self.estado)
        elif self.estado == 'Baja':
            return format_html('<span style="background-color:#a00; color:#fff;padding:5px;">{}</span>', self.estado)
    
    def delete(self,using=None,keep_parents=False):
        self.url_img.storage.delete(self.url_img.name)
        super().delete()


class Gastronomia(CardABS):

    url_img = models.ImageField(upload_to = "Gastronomia/", blank= True, null= True)

    def __str__(self):
        return self.nombre
    
    # def soft_delete(self):
    #     self.baja=True
    #     super().save()
    
    # def restore(self):
    #     self.baja=False
    #     super().save()

    class Meta():
        verbose_name_plural='Gastronomias'

class Actividades(CardABS):

    url_img = models.ImageField(upload_to = "Actividades/", blank= True, null= True)

    def __str__(self):
        return self.nombre
    
    # def soft_delete(self):
    #     self.baja=True
    #     super().save()
    
    # def restore(self):
    #     self.baja=False
    #     super().save()

    class Meta():
        verbose_name_plural='Actividades'

class PuntosInteres(CardABS):

    url_img = models.ImageField(upload_to = "PuntosInteres/", blank= True, null= True)


    def __str__(self):
        return self.nombre
    
    # def soft_delete(self):
    #     self.baja=True
    #     super().save()
    
    # def restore(self):
    #     self.baja=False
    #     super().save()

    class Meta():
        verbose_name_plural='Puntos de Interes'

class ZonasAlojamientos(CardABS):

    url_img = models.ImageField(upload_to = "ZonasAlojamientos/", blank= True, null= True)

    def __str__(self):
        return self.nombre
    
    # def soft_delete(self):
    #     self.baja=True
    #     super().save()
    
    # def restore(self):
    #     self.baja=False
    #     super().save()

    class Meta():
        verbose_name_plural='Zonas de Alojamiento'

class TipoConsulta(models.Model):
    asunto = models.CharField(max_length=50, verbose_name='asunto')

    def __str__(self):
        return self.asunto


class Consulta(models.Model):

    CONTESTADA = 'Contestada'
    NOCONTESTADA = 'No Contestada'
    ENPROCESO = 'En proceso'

    ESTADOS = (
        (CONTESTADA, 'Contestada'),
        (NOCONTESTADA, 'No Contestada'),
        (ENPROCESO, 'En proceso'),
    )

    nombre = models.CharField(max_length=100,validators=(solo_caracteres,),verbose_name='nombre_completo')
    telefono = models.IntegerField(verbose_name='telefono')
    email = models.EmailField(max_length=50, verbose_name='email')
    asunto = models.ForeignKey(TipoConsulta,on_delete=models.CASCADE,verbose_name='asunto')
    mensaje = models.CharField(max_length=400,verbose_name='mensaje', validators=(clean_mensaje,))
    estado_respuesta = models.CharField(max_length=15, blank=True, null=True, choices=ESTADOS, default= NOCONTESTADA) 
     
    fecha = models.DateField(default=datetime.now, blank=True, editable=True) 

   
    def estado_de_respuesta(self,):
        if self.estado_respuesta == 'Contestada':
            return format_html('<span style="background-color:#0a0; color:#fff;padding:5px;">{}</span>', self.estado_respuesta)
        elif self.estado_respuesta == 'No Contestada':
            return format_html('<span style="background-color:#a00; color:#fff;padding:5px;">{}</span>', self.estado_respuesta)
        elif self.estado_respuesta == 'En proceso':
            return format_html('<span style="background-color:#FOB203; color:#000;padding:5px;">{}</span>', self.estado_respuesta)

    def __str__(self):
        return f'Consulta de {self.nombre}' 
    
    class Meta():
        verbose_name_plural='Consultas'

class Respuesta(models.Model):

    consulta = models.ForeignKey(Consulta(), blank=True, null=True, on_delete=models.CASCADE)
    respuesta = models.TextField(blank=False, null=False)
    fecha = models.DateField(default=datetime.now, blank=True, null=True) 

    def create_mensaje(self,):
        consulta_cambio_estado = Consulta.objects.get(id=self.consulta.id)
        consulta_cambio_estado.estado_respuesta = 'Contestada'
        consulta_cambio_estado.save()

        #LOGICA DE ENVIO DE MAIL
        
        mail = create_mail(
        consulta_cambio_estado.email,
        'Respuesta a Solicitud Web Turismo Tornquist',
        'tornquist/publica/email.html',
        {
            'username': consulta_cambio_estado.nombre,
            'mensaje': self.respuesta
        }
        )

        mail.send(fail_silently=False)

    def save(self, *args, **kwargs):
        self.create_mensaje()
        force_update = False
        if self.id:
            force_update = True
        super(Respuesta, self).save(force_update=force_update)

class Solicitud(models.Model):

    class Meta:
        verbose_name_plural = 'Solicitudes'

    ACEPTADA    = 'Aceptada'
    RECHAZADA   = 'Rechazada'
    ENREVISION  = 'En revision'

    ESTADOS = (
        (ACEPTADA, 'Aceptada'),
        (RECHAZADA, 'Rechazada'),
        (ENREVISION, 'En revision'),
    )
    RUBROS = [
        ("", "Seleccione un rubro"),
        ("Gastronomia", "Gastronomia"),
        ("Actividades", "Actividades"),
        ("Puntos de interes", "Puntos de interes"),
        ('Alojamiento','Alojamiento'),
        ]
        
    UBICACIONES = [
            ("", "Seleccione una ubicacion"),
            ("Tornquist", "Tornquist"),
            ("Sierra de la ventana", "Sierra de la ventana"),
        ]

    nombre = models.CharField(max_length=50) 
    ubicacion = models.CharField(max_length=200, choices=UBICACIONES)
    rubro = models.CharField(max_length=20, choices=RUBROS)
    direccion = models.CharField(max_length=50)
    estado_respuesta = models.CharField(max_length=15, choices=ESTADOS, default= ENREVISION) 
    sitio = models.CharField(max_length=50,)
    telefono = models.CharField(max_length=50) 
    imagen = models.ImageField(upload_to = carpetas_de_guardado, blank=True, editable=True, validators=[valid_extension])
    fecha = models.DateField(default=datetime.now, blank=True, editable=True) 

    def __str__(self) -> str:
        return self.nombre

    def estado_de_respuesta(self,):
        if self.estado_respuesta == 'Aceptada':
            return format_html('<span style="background-color:#0a0; color:#fff;padding:5px;">{}</span>', self.estado_respuesta)
        elif self.estado_respuesta == 'Rechazada':
            return format_html('<span style="background-color:#a00; color:#fff;padding:5px;">{}</span>', self.estado_respuesta)
        elif self.estado_respuesta == 'En revision':
            return format_html('<span style="background-color:#0000ff; color:#fff;padding:5px;">{}</span>', self.estado_respuesta)
        
class RespuestaSolicitud(models.Model):

    solicitud = models.ForeignKey(Solicitud(), blank=True, null=True, on_delete=models.CASCADE)
    respuesta = models.TextField(blank=False, null=False)
    estado_solicitud = models.CharField(max_length=15, blank=True, null=True, choices=Solicitud.ESTADOS)
    fecha = models.DateField(default=datetime.now, blank=True, null=True) 

    def create_mensaje(self,):
        solicitud_cambio_estado = Solicitud.objects.get(id=self.solicitud.id)
        solicitud_cambio_estado.estado_respuesta = self.estado_solicitud
        solicitud_cambio_estado.save()
        #LOGICA DE ENVIO DE MAIL
        
    def generar_registro(self, rubro, solicitud):
        rubros = {
            'gastronomia':Gastronomia(),
            'actividades':Actividades(),
            'interes':PuntosInteres(),
            'alojamiento':ZonasAlojamientos(),

        }
        if rubro in rubros:
            instancia = rubros[rubro]

        instancia.nombre    = solicitud.nombre
        instancia.ubicacion = solicitud.ubicacion
        instancia.telefono  = solicitud.telefono
        instancia.direccion = solicitud.direccion
        instancia.sitio     = solicitud.sitio
        instancia.imagen    = solicitud.imagen
        instancia.estado    = solicitud.estado_respuesta
        instancia.save()

    # def eliminar_registro(self, rubro, solicitud):
    #     rubros = {
    #         'gastronomia':Gastronomia(),
    #         'actividades':Actividades(),
    #         'interes':PuntosInteres(),
    #         'alojamiento':ZonasAlojamientos(),

    #     }
    #     if rubro in rubros:
    #         instancia = rubros[rubro]

    #     instancia.delete()        

    def create_entidad(self,):
        get_estado_solicitud = Solicitud.objects.get(id=self.solicitud.id)
        if get_estado_solicitud.estado_respuesta == 'Aceptada':
            if get_estado_solicitud.rubro == "Gastronomia":
                self.generar_registro('gastronomia', get_estado_solicitud)
            elif get_estado_solicitud.rubro == "Actividades":
                self.generar_registro('actividades', get_estado_solicitud)
            elif get_estado_solicitud.rubro == "Puntos de interes":
                self.generar_registro('interes', get_estado_solicitud)
            elif get_estado_solicitud.rubro == "Alojamiento":
                self.generar_registro('alojamiento', get_estado_solicitud)
        # else:
        #     self.eliminar_registro()    

    def save(self, *args, **kwargs):
        self.create_mensaje()
        self.create_entidad()
        force_update = False
        if self.id:
            force_update = True
        super(RespuestaSolicitud, self).save(force_update=force_update)

