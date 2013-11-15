# Create your views here.
from django.shortcuts import render_to_response
from Miblog.models import Articulos
def home(request):
	# contenido = {
	# 	'titulo' : 'Mi primer Articulo',
	# 	'author' : 'Ronald Loyola',
	# 	'fecha' : '08 de Octubre 2013',
	# 	'contenido' : 'aqui va el contenido ....',
	# }
	entradas = Articulos.objects.all()[:10]

	# return render_to_response('index.html',contenido)

	return render_to_response('index.html',{'articulos' : entradas})

