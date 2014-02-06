# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext # importante para reutilizar user en la vista
from Miblog.models import Articulos
from forms import ArticulosForm, LoginForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth import login, logout, authenticate

def home(request):
	# contenido = {
	# 	'titulo' : 'Mi primer Articulo',
	# 	'author' : 'Ronald Loyola',
	# 	'fecha' : '08 de Octubre 2013',
	# 	'contenido' : 'aqui va el contenido ....',
	# }
    #Muestra 10 articulos como maximo desde la base de datos
	entradas = Articulos.objects.all()[:10]

	# return render_to_response('index.html',contenido)

	return render_to_response('index.html',{'articulos' : entradas},context_instance=RequestContext(request))

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
  return render_to_response('index.html', {'articulos' : Articulos.objects.all() },context_instance=RequestContext(request))

def articulo(request, articulo_id=1):
  return render_to_response('articulo.html', {'articulo' : Articulos.objects.get(id=articulo_id) },context_instance=RequestContext(request))

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                next = request.POST['next']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect(next)
                else:
                    mensaje = "usuario y/o password incorrecto"
        next = request.REQUEST.get('next')
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje,'next':next}
        return render_to_response('login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
