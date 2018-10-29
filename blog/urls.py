from django.conf.urls import include, url
from .views import Contacto
from .views import Mascotas


urlpatterns = [
    url(r'^contacto', Contacto, name='Contacto'),
    url(r'^mascota', Mascotas, name='Mascota'),
    ]
