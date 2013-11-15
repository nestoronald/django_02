from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('',
    url(r'^todos/$', 'Miblog.views.articulos'),
    url(r'^obtener/(?P<articulo_id>\d+)/$', 'Miblog.views.articulo'),
)
