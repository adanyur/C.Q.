from rest_framework import serializers
from ..models.participantes import *


class TipoParticipantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoParticipanteModel
        fields = '__all__'
        # extra_kwargs = {'id': {'validators': []},}



class ParticipantesSerializers(serializers.ModelSerializer):
    descripcion = TipoParticipantesSerializers()
    # descripcion = TipoParticipantesSerializers(many=True)
    
    class Meta:
        model = ParticipantesModel
        fields = ('cq_codiqx','cq_numero','cq_codpar','descripcion')
        # fields = ('cq_codiqx','cq_numero','cq_codpar')
    