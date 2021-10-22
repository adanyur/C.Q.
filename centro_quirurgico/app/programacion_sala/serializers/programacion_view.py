from rest_framework import serializers
from ..models.programacion_view import *


'''SERIALIZER PARA HACER LAS RELACIONES'''

class IntervencionSerializers(serializers.ModelSerializer):
    class Meta:
        model = IntervencionViewModel
        fields = ('cq_codiqx','cq_nomint')
        read_only_fields = fields

class CamasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamasViewModel
        fields = ('ch_codigo','ch_descripcion')
        read_only_fields = fields

class SalasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalasViewModel
        fields = ('sa_codsal','sa_nombre')
        read_only_fields = fields


class TipoParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeParticipantesViewModel
        fields = ('cq_codpar','cq_despar')
        read_only_fields = fields

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspecialidadViewModel
        fields = ('es_codigo','cq_dees_descripcionspar')
        read_only_fields = fields


'''SERIALIZER CABECERA Y DETALLE'''

class ProgramacionViewDetalleSerializer(serializers.ModelSerializer):
    cq_codpar =  serializers.StringRelatedField()
    class Meta:
        model = ProgramacionDetalleViewModel
        fields = ('cq_numero', 'cq_codpar', 'pl_codper')
        read_only_fields = fields


class ProgramacionViewSerializer(serializers.ModelSerializer):
    sa_codsal = SalasSerializer()
    cq_cama = serializers.StringRelatedField()
    cq_codiqx = serializers.StringRelatedField()
    cq_codiqx2 = serializers.StringRelatedField()
    cq_codiqx3 = serializers.StringRelatedField()
    se_codigo = serializers.StringRelatedField()

    detalle  = ProgramacionViewDetalleSerializer(many=True)
    class Meta:
        model = ProgramacionViewModel
        fields = '__all__'