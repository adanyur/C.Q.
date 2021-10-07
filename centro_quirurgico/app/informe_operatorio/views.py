from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# 
from .models import *
from .serializers import *


def validacionDeInforme(numeroDeOperacion):
    return InformeOperatorio.objects.filter(cq_numope=numeroDeOperacion).first()

@api_view(['POST'])
def informe_operatorio_api_view(request):
    if request.method == 'POST':
        if validacionDeInforme(request.data['cq_numope']):
            return Response({'message':'EL Informe Operatorio ya esta registrado'},status=status.HTTP_400_BAD_REQUEST)
        serializer = InformeOperatorioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Se registro correctamente!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT'])
def informe_operatorio_detalle_api_view(request,pk):
        informeOperatorio_data = InformeOperatorio.objects.filter(cq_numope=pk).first()
        if informeOperatorio_data:
            if request.method == 'GET':
                serializer = InformeOperatorioSerializers(informeOperatorio_data)
                return Response(serializer.data)
                
            if request.method == 'PUT':
                informeOperatorio_serializer = InformeOperatorioSerializers(informeOperatorio_data,data=request.data)
                if informeOperatorio_serializer.is_valid():
                    informeOperatorio_serializer.save()
                    return Response({'message':'Se actualizo correctamente'})
        return Response({'message':'No se encontro datos'},status=status.HTTP_400_BAD_REQUEST)

