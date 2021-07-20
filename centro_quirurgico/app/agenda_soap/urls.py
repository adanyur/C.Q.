from django.urls import path
from .views import *

urlpatterns = [
    path('', camas_api_view),
]