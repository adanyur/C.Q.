from rest_framework import serializers
from ..models.programacion_cq import *



class ProgramacionDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionParticipantesModel
        fields = '__all__'
        extra_kwargs = {'id': {'validators': []},}


class EquiposMedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionEquiposMedicosModel
        fields = '__all__'
        extra_kwargs = {'id': {'validators': []},}


class ProgramacionSerializer(serializers.ModelSerializer):
    participantes = ProgramacionDetalleSerializer(many=True)
    equiposMedicos = EquiposMedicosSerializer(many=True)

    class Meta:
        model = ProgramacionModel
        fields = ('cq_numope','sa_codsal','cq_estancia','equiposMedicos','participantes')

    #create
    def create(self, validated_data):
        equiposMedicos = validated_data.pop('equiposMedicos')    
        participantes = validated_data.pop('participantes')

        '''Programacion'''
        programacion = ProgramacionModel.objects.create(**validated_data)

        '''Participantes '''
        
        for participantes in participantes:
            ProgramacionParticipantesModel.objects.create(cq_numope=programacion, **participantes)

        '''Equipos Medicos'''
        
        for equiposMedicos in equiposMedicos:
            ProgramacionEquiposMedicosModel.objects.create(de_numope=programacion, **equiposMedicos)
        return programacion

    #update
    def update(self, instance,validated_data):

        participantes = validated_data.pop('participantes')
        participantes_queryset = (instance.participantes).all()
        detalleDeParticipantes = list(participantes_queryset) 

        equiposMedicos = validated_data.pop('equiposMedicos')
        equiposMedicos_queryset = (instance.equiposMedicos).all()

        ''' Programacion '''
        #Actualiza la programacion
        instance.cq_numope = validated_data.get('cq_numope', instance.cq_numope)
        instance.sa_codsal = validated_data.get('sa_codsal', instance.sa_codsal)
        instance.cq_estancia = validated_data.get('cq_estancia', instance.cq_estancia)
        instance.save()
        
        ''' Equipos medicos '''
        #Elimina todo el detale de equipos medicos
        equiposMedicos_queryset.delete()
        for equiposMedicos in equiposMedicos:
            ProgramacionEquiposMedicosModel.objects.create(**equiposMedicos)


        ''' Participantes'''
        #Actualiza a los participantes
        for participantes in participantes:
            keys = detalleDeParticipantes.pop(0)
            keys.cq_numope = participantes.get('cq_numope',keys.cq_numope)
            keys.sa_codsal = participantes.get('sa_codsal',keys.sa_codsal)
            keys.se_codigo = participantes.get('se_codigo',keys.se_codigo)
            keys.cq_codiqx = participantes.get('cq_codiqx',keys.cq_codiqx)
            keys.ar_codare = participantes.get('ar_codare',keys.ar_codare)
            keys.pl_codper = participantes.get('pl_codper',keys.pl_codper)
            keys.cq_estado = participantes.get('cq_estado',keys.cq_estado)
            keys.cq_observ = participantes.get('cq_observ',keys.cq_observ) 
            keys.save()

        return instance