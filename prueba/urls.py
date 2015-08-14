
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), 
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^redactor/', include('redactor.urls')),
    url(r'^',include('events.urls',namespace="events")),
    url(r'^',include('users.urls',namespace="users")),
    url('', include('social.apps.django_app.urls',namespace='social')),

    
]
