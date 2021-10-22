from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
#
from ..models.programacion_view import *
from ..serializers.programacion_view import *


@api_view(['GET'])
def programacion_view(request,pk):
    programacion_data = ProgramacionViewModel.objects.filter(cq_numope=pk).first()
    if programacion_data:
        if request.method == 'GET':
            programacion_serializer = ProgramacionViewSerializer(programacion_data)
            return Response(programacion_serializer.data,status=status.HTTP_200_OK)
    return Response({"message":"No se encontro dato"},status=status.HTTP_400_BAD_REQUEST)
       