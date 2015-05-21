from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^articulos/', include('Miblog.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    # Examples:
    # url(r'^$', 'django_02.views.home', name='home'),
    # url(r'^django_02/', include('django_02.foo.urls')),
    url(r'^$','Miblog.views.home', name='home'),
    url(r'^login/$', 'Miblog.views.login_view', name="vista_login"),
    url(r'^logout/$', 'Miblog.views.logout_view', name="vista_logout"),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^crear/', 'Miblog.views.crear', name='crear'),

)
