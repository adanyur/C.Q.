from rest_framework import serializers
from .models import *


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = '__all__'

