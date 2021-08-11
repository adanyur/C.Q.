from rest_framework import serializers
from ..models.personales import *

class PersonalSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField(source='pl_codper')
    nombre = serializers.CharField(source='nombre_personal')
    tipo = serializers.CharField(default='A')

    class Meta:
        model = Personales
        fields = ['codigo','nombre','tipo']


class MedicosSerializers(serializers.ModelSerializer):
    codigo = serializers.CharField(source='me_codigo')
    nombre = serializers.CharField(source='me_nombres')
    tipo = serializers.CharField(default='M')
    class Meta:
        model = Medicos
        fields = ['codigo','nombre','tipo']
        read_only_fields = fields