
from django.conf.urls import  url
from django.contrib import admin
from .views import index, panel, crearevento, detalle, editar, eliminar
from braces.views import LoginRequiredMixin

urlpatterns = [

    
    url(r'^$', index.as_view(),name='index'),
    url(r'^panel/$', panel.as_view(),name='panel'),
      url(r'^panel/nuevo/$', crearevento.as_view(),name='crearevento'),
     url(r'^panel/evento/(?P<pk>\d+)/$', detalle.as_view(),name="detalle"),
     url(r'^panel/evento/editar/(?P<pk>\d+)/$', editar.as_view(),name="editar"),
     url(r'^panel/evento/eliminar/(?P<pk>\d+)/$', eliminar.as_view() ,name="eliminar"),
     url(r'^evento-ajax/$', 'events.views.eventoajax'),




]