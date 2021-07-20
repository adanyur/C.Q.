from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#
from .models import ProgramacionSOAP
from .serializers import ProgramacionSOAPSerializer


@api_view(['GET'])
def camas_api_view(request):
    
    if request.method == 'GET':
        data = ProgramacionSOAP.objects.raw("SELECT * FROM cq_c_programacion('19/05/2021')")
        ProgramacionSOAP_serializer = ProgramacionSOAPSerializer(data,many=True)
        return Response(ProgramacionSOAP_serializer.data)
