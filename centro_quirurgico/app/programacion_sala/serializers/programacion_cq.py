from rest_framework import serializers
from ..models.programacion_cq import *




class ProgramacionDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionDetalleModel
        fields = '__all__'


class ProgramacionSerializer(serializers.ModelSerializer):
    programacion_detalle = ProgramacionDetalleSerializer(many=True)
    class Meta:
        model = ProgramacionModel
        fields = ('cq_numope','sa_codsal','cq_estancia','programacion_detalle')

    def create(self, validated_data):
        programacion = ProgramacionModel.objects.create(**validated_data)
        programacionDetalle = validated_data.pop('programacion_detalle')
        for programacionDetalle in programacionDetalle:
            ProgramacionDetalleModel.objects.create(cq_numope=programacion, **programacionDetalle)
        return programacion

    def update(self, instance,validated_data):
        programacionDetalleData = validated_data.pop('programacion_detalle')   
        programacionDetalle = (instance.programacion_detalle).all()
        programacionDetalle = list(programacionDetalle)

        # for programacionDetalleData in programacionDetalleData:
        #     item = programacionDetalle.pop(0)
        #     item.cq_numope = programacionDetalleData.get('cq_numope','0000000000')
        #     # item.save()

        instance.cq_numope = validated_data.get('cq_numope', instance.cq_numope)
        instance.sa_codsal = validated_data.get('sa_codsal', instance.sa_codsal)
        instance.cq_estancia = validated_data.get('cq_estancia', instance.cq_estancia)
        instance.save()
        return instance
        



        # instance.cq_numope = validated_data.get('cq_numope', instance.cq_numope)
        # instance.sa_codsal = validated_data.get('sa_codsal', instance.sa_codsal)
        # instance.cq_estancia = validated_data.get('cq_estancia', instance.cq_estancia)
        # instance.save()



     # for detalle in programacionDetalleData:
        #     detail = programacionDetalle.pop(0)
        #     detail.cq_numope = detalle.get('cq_numope',detail.cq_numope)
        #     detail.sa_codsal = detalle.get('sa_codsal',detail.sa_codsal)
        #     detail.se_codigo = detalle.get('se_codigo',detail.se_codigo)
        #     detail.cq_codiqx = detalle.get('cq_codiqx',detail.cq_codiqx)
        #     detail.ar_codare = detalle.get('ar_codare',detail.ar_codare)
        #     detail.pl_codper = detalle.get('pl_codper',detail.pl_codper)
        #     detail.cq_estado = detalle.get('cq_estado',detail.cq_estado)
        #     detail.cq_observ = detalle.get('cq_observ',detail.cq_observ) 
        #     detail.save()