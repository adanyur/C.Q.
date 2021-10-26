from django.urls import path, include
from django.conf.urls import url
#
from .views import *

urlpatterns = [    
    url(r'^incidencia/(?P<pk>\d+)/$', incidencia_detail_api_view),
    url(r'^incidencias',incidencia_api_view),
]