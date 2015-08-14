
from django.conf.urls import  url
from django.contrib import admin



urlpatterns = [

    url(r'^users/nuevo/','users.views.userlogin' ,name='login'),
     url(r'^salir/','users.views.Logout' ,name='salir'),
 
    
]