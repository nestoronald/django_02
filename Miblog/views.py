# Create your views here.
from django.shortcuts import render_to_response
from Miblog.models import Articulos
from forms import ArticulosForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
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

def crear(request):
    if request.POST:
        form = ArticulosForm(request.POST)
        if form.is_valid():
            form.save()
 
            return HttpResponseRedirect('/')
    else:
        form = ArticulosForm()
     
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render_to_response('crear_articulo.html', args)

def articulos(request):
  return render_to_response('index.html', {'articulos' : Articulos.objects.all() })
 
def articulo(request, articulo_id=1):
  return render_to_response('articulo.html', {'articulo' : Articulos.objects.get(id=articulo_id) })