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

class Continent(models.Model):
    continent = models.CharField(max_length=100)

    def __unicode__(self):  # Python 3: def __str__(self):
        return unicode(self.continent)

class Country(models.Model):
    country = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent)

    def __unicode__(self):  # Python 3: def __str__(self):
        return unicode(self.country)

# class Location(models.Model)
#     continent = models.ForeignKey(Continent)
#     country = models.ForeignKey(Country)
#     area = models.ForeignKey(Area)
#     city = models.CharField(max_length=50)
#     street = models.CharField(max_length=100)

from smart_selects.db_fields import ChainedForeignKey 

class Location(models.Model):
    continent = models.ForeignKey(Continent)
    country = ChainedForeignKey(Country,chained_field="continent",chained_model_field="continent",show_all=False,auto_choose=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    def __unicode__(self):  # Python 3: def __str__(self):
        return unicode(self.city)