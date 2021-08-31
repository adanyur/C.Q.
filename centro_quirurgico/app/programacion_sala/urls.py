from django.urls import path, include
from django.conf.urls import url
#
from .views.intervencion import *
from .views.anestesia import *
from .views.disponibilidad_salas import *
from .views.personales import *
from .views.programacion_cq import *
from .views.participantes import *

urlpatterns = [
    url(r'^anestesia', anestesia_api_view),
    url(r'^intervencion', intervencion_api_view),
    url(r'^sala', disponibilidad_salas_api_view),
    url(r'^personales', personales_api_view),
    url(r'^programaciones', programaciones_api_view),    
    url(r'^programacion/(?P<pk>\d+)/$',programacion_detalle_api_view),
    url(r'^participantes',participantes_api_view)
    
]