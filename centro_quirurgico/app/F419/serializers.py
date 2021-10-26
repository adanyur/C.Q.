from rest_framework import serializers
from .models import *


class F419DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = F419DetailModel
        fields = ('tipo','value','usuario')


class F419Serializer(serializers.ModelSerializer):
    detalles = F419DetailSerializer(many=True)
    class Meta:
        model = F419Model
        fields = '__all__'

    #create
    def create(self, validated_data):
        detalles = validated_data.pop('detalles')
        '''Cabecera de la Incidencias'''
        f419 = F419Model.objects.create(**validated_data)
        '''Detalle de la Incidencias'''
        for detalles in detalles:
            F419DetailModel.objects.create(id_cabecera=f419, **detalles)
        return f419

    #actualizar
    def update(self, instance,validated_data):
        detalles = validated_data.pop('detalles')
        detalles_queryset = (instance.detalles).all()

        instance.fecha=validated_data.get('fecha',instance.fecha)
        instance.historia=validated_data.get('historia',instance.historia)
        instance.glosa=validated_data.get('glosa',instance.glosa)
        instance.turno=validated_data.get('turno',instance.turno)
        instance.usuario=validated_data.get('usuario',instance.usuario)
        instance.fecha_registro=validated_data.get('fecha_registro',instance.fecha_registro)
        instance.usuario_actualizado=validated_data.get('usuario_actualizado',instance.usuario_actualizado)
        instance.fecha_actualizado=validated_data.get('fecha_actualizado',instance.fecha_actualizado)
        instance.save()

        detalles_queryset.delete()
        for detalles in detalles:
            F419DetailModel.objects.create(**detalles)
        return instance