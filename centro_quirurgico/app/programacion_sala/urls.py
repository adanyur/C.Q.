from django.conf.urls import url
from .views.intervencion import *
from .views.anestesia import *

urlpatterns = [
    url(r'^anestesia', anestesia_api_view),
    url(r'^intervencion', intervencion_api_view),
]