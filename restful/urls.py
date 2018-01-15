from django.conf.urls import url, include
from django.contrib import admin
import os
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =  [
    url(r'^', include('apps.restful_app.urls'))
 ] 

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_URL = '/static/'
