from django.conf.urls import include, url
from . import views           
urlpatterns = [
    url(r'^$', views.loginregpage),
    url(r'^login$', views.login),
    url(r'^registration$', views.registration),
    url(r'^usersindex$', views.usersindex),
    url(r'^(?P<id>\d+)/edit$', views.edituser),
    url(r'^showuser/(?P<id>\d+)$', views.showuser),
    url(r'^users/(?P<id>\d+)/edit$', views.rendereditpage),
    url(r'^comment/(?P<id>\d+)$', views.makecomment),
    url(r'^post/(?P<id>\d+)$', views.makepost),
    url(r'^removepost/(?P<id>\d+)$', views.removepost),
    url(r'^removecomment/(?P<id>\d+)$', views.removecomment),
    url(r'^logoff$', views.logoff)



 ]

 

