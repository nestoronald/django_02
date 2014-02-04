from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulos(models.Model):
	author = models.CharField(max_length = 30)
	titulo = models.CharField(max_length = 100)
	texto = models.TextField()
	fecha = models.DateTimeField()

class Comentarios(models.Model):
   nombre = models.CharField(max_length = 200)
   cuerpo = models.TextField()
   fecha_pub = models.DateTimeField('fecha publicacion')
   articulo = models.ForeignKey(Articulos)

class Perfil(models.Model):
    user = models.OneToOneField(User)
    telefono = models.CharField(max_length=300)
    direccion = models.TextField()
    def __unicode__(self):
        return self.user.username
