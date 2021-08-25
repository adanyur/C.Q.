from rest_framework import serializers
from ..models.programacion_cq import *




class ProgramacionDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionDetalleModel
        fields = ['cq_numope','cq_numero','cq_codpar']




class ProgramacionSerializer(serializers.ModelSerializer):
    # programacion_detalle = ProgramacionDetalleSerializer(many=True,read_only=True)
    programacion_detalle = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProgramacionModel
        fields = ['cq_numope','sa_codsal','cq_estancia','cq_fecha','programacion_detalle']
        # read_only_fields = ['cq_numope']
