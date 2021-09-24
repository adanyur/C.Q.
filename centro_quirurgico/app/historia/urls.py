from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [    
    path('searchpaciente',HistoriaSearch.as_view()),
    url(r'^historia/(?P<pk>\d+)/$',historias_api_view)
]