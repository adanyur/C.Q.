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
    equipos_medicos = EquiposMedicosSerializer(many=True)
    programacion_detalle = ProgramacionDetalleSerializer(many=True)

    class Meta:
        model = ProgramacionModel
        fields = ('cq_numope','sa_codsal','cq_estancia','equipos_medicos','programacion_detalle')

    #create
    def create(self, validated_data):
        programacionDetalle = validated_data.pop('programacion_detalle')
        equiposMedicos = validated_data.pop('equipos_medicos')
        programacion = ProgramacionModel.objects.create(**validated_data)

        for programacionDetalle in programacionDetalle:
            ProgramacionParticipantesModel.objects.create(cq_numope=programacion, **programacionDetalle)

        for equiposMedicos in equiposMedicos:
            ProgramacionEquiposMedicosModel.objects.create(de_numope=programacion, **equiposMedicos)

        return programacion

    #update
    def update(self, instance,validated_data):
        programacionDetalleData = validated_data.pop('programacion_detalle')   
        equiposMedicos = validated_data.pop('equipos_medicos')
        programacionDetalle = (instance.programacion_detalle).all()
        programacionDetalle = list(programacionDetalle)

        instance.cq_numope = validated_data.get('cq_numope', instance.cq_numope)
        instance.sa_codsal = validated_data.get('sa_codsal', instance.sa_codsal)
        instance.cq_estancia = validated_data.get('cq_estancia', instance.cq_estancia)
        instance.save()

        for detalle in programacionDetalleData:
            items = programacionDetalle.pop(0)
            items.cq_numope = detalle.get('cq_numope',items.cq_numope)
            items.sa_codsal = detalle.get('sa_codsal',items.sa_codsal)
            items.se_codigo = detalle.get('se_codigo',items.se_codigo)
            items.cq_codiqx = detalle.get('cq_codiqx',items.cq_codiqx)
            items.ar_codare = detalle.get('ar_codare',items.ar_codare)
            items.pl_codper = detalle.get('pl_codper',items.pl_codper)
            items.cq_estado = detalle.get('cq_estado',items.cq_estado)
            items.cq_observ = detalle.get('cq_observ',items.cq_observ) 
            items.save()

        return instance