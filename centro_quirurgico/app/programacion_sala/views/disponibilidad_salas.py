from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
#
from ..models.disponibilidad_salas import *
from ..serializers.disponibilidad_salas import *


@api_view(['GET'])
def disponibilidad_salas_api_view(request,sala,fecha):
        if request.method == 'GET':
            print({sala,fecha})
            disponibilidad_sala = DisponibilidadSalas.objects.raw("SELECT * FROM cq_c_disponibilidad_salas('{0}','{1}')".format(fecha,sala))
            disponibilidad_serializers = DisponibilidadSalasSerializer(disponibilidad_sala,many=True)
            return Response(disponibilidad_serializers.data)