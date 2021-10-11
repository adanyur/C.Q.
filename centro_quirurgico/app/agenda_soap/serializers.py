from rest_framework import serializers
from .models import ProgramacionSOAP

class ProgramacionSOAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionSOAP
        fields = ('diahora',
                'sala',
                'paciente',
                'intervencion',
                'cirujano',
                'anestesia',
                'cama',
                'pedido',
                'cq_numope',
                'cq_fecha',
                'cq_hoinpr',
                'cq_hofipr',
                'cq_hoinej',
                'cq_hofiej',
                'cq_numhis',
                'cq_estado',
                'edad',
                'semanas',
                'tiempo',
                'inf_ope')
        read_only_fields = fields