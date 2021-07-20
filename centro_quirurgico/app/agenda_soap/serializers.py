from rest_framework import serializers
from .models import Camas

class CamasSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Camas
        fields = '__all__'