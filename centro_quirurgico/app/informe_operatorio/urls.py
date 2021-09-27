from django.urls import path, include
from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^informeoperatorio', informe_operatorio_api_view),
]