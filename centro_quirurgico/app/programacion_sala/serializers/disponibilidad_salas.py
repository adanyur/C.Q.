from rest_framework import serializers
from ..models.disponibilidad_salas import *


class DisponibilidadSalasSerializer(serializers.ModelSerializer):
     class Meta:
        model = DisponibilidadSalas
        fields = ('id','hora','descripcion','estado')
        read_only_fields = fields