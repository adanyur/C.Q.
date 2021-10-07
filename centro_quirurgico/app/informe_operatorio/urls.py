from django.urls import path, include
from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^informeoperatoriodata/(?P<pk>\d+)/$',informe_operatorio_detalle_api_view),
    url(r'^informeoperatorio', informe_operatorio_api_view),
]