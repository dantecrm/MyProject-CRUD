from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'crud.views.inicio', name="inicio"),
    url(r'^agregar/$', 'crud.views.agregar', name="agregar"),
    url(r'^editar/(?P<id>\d+)$', 'crud.views.editar', name="editar"),
    url(r'^borrar/(?P<id>\d+)$', 'crud.views.borrar', name="borrar"),
)
