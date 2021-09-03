from django.db.models import Max
#
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
#
from ..models.programacion_cq import *
from ..serializers.programacion_cq import *


@api_view(['POST'])
def programaciones_api_view(request):
    #Se obtiene el maximo numero de operacion
    data = ProgramacionModel.objects.aggregate(cq_numope=Max('cq_numope'))
    #Se genera el correlativo de numero de operacion
    numeroOperacion = str(int(data['cq_numope']) + 1).rjust(10,'0')
    if request.method == 'POST':
        request.data['cq_numope'] = numeroOperacion
        for data in request.data['participantes']:
            data['sa_codsal']=request.data['sa_codsal']          
        serializer = ProgramacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Se registro correctamente!!'})
        return Response(serializer.errors)


@api_view(['GET','PUT'])
def programacion_detalle_api_view(request,pk):
    programacion_data = ProgramacionModel.objects.filter(cq_numope=pk).first()

    if programacion_data :
        if request.method == 'GET':
            programacion_serializer = ProgramacionSerializer(programacion_data)            
            return Response(programacion_serializer.data)
        if request.method == 'PUT':
            programacion_serializer = ProgramacionSerializer(programacion_data,data = request.data)
            if programacion_serializer.is_valid():
                programacion_serializer.save()
                return Response({'message':'Se actualizo correctamente!!'})
            return Response(programacion_serializer.errors)
    return Response({'message':'No se encontro datos'})