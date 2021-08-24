from rest_framework import serializers
from ..models.programacion_cq import *


class ProgramacionCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionCQ        
        fields = '__all__'