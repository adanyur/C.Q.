from django.conf.urls import url
from .views.intervencion import *
from .views.anestesia import *
from .views.disponibilidad_salas import *
from .views.personales import *
from .views.programacion_cq import *

urlpatterns = [
    url(r'^anestesia', anestesia_api_view),
    url(r'^intervencion', intervencion_api_view),
    url(r'^sala', disponibilidad_salas_api_view),
    url(r'^personales', personales_api_view),
    url(r'^programacion', programacion_cq_api_view),
]