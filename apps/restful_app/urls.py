from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^users$', views.usersindex),
    url(r'^users/create$', views.newuser),
    url(r'^process$', views.process),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^users/(?P<id>\d+)/show$', views.showuser),
    url(r'^users/(?P<id>\d+)/edit$', views.edituser),
    url(r'^users/(?P<id>\d+)/delete$', views.deleteuser)
 ]

