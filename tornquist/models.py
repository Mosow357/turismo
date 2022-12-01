from django.db import models

# Create your models here.

class CardABS(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre')
    ubicacion = models.CharField(max_length=150,verbose_name='ubicacion')
    telefono = models.CharField(max_length=150,verbose_name='telefono')
    direccion = models.CharField(max_length=150,verbose_name='direccion')
    pagina_web = models.CharField(max_length=150,verbose_name='pagina_web')
    url_img = models.ImageField(upload_to='imagenes/', max_length=200,verbose_name='url_img')
    baja = models.BooleanField(default=0)

    class Meta:
        abstract = True
    
    def delete(self,using=None,keep_parents=False):
        self.url_img.storage.delete(self.url_img.name)
        super().delete()


class Gastronomia(CardABS):

    def __str__(self):
        return self.nombre
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

    class Meta():
        verbose_name_plural='Gastronomias'

class Actividades(CardABS):
    def __str__(self):
        return self.nombre
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

    class Meta():
        verbose_name_plural='Actividades'

class PuntosInteres(CardABS):
    def __str__(self):
        return self.nombre
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

    class Meta():
        verbose_name_plural='Puntos de Interes'

class ZonasAlojamientos(CardABS):
    def __str__(self):
        return self.nombre
    
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

    class Meta():
        verbose_name_plural='Zonas de Alojamiento'

class TipoConsulta(models.Model):
    asunto = models.CharField(max_length=50, verbose_name='asunto')

    def __str__(self):
        return self.asunto


class Consulta(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre_completo')
    telefono = models.IntegerField(verbose_name='telefono')
    email = models.EmailField(max_length=50, verbose_name='email')
    asunto = models.ForeignKey(TipoConsulta,on_delete=models.CASCADE,verbose_name='asunto')
    mensaje = models.CharField(max_length=400,verbose_name='mensaje')
    respondido = models.BooleanField(default=0)

    def __str__(self):
        return f'Consulta de {self.nombre}' 
    
    class Meta():
        verbose_name_plural='Consultas'