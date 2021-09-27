from rest_framework import serializers
from .models import *


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ('hc_numhis','hc_apepat','hc_apemat','hc_nombre','hc_fecnac','hc_sexo')
        read_only_fields = fields


class Cie10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cie10
        fields = ('codigo','descripcion')
        read_only_fields = fields