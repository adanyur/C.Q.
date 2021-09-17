from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [    
    path('historia',HistoriaSearch.as_view())
]