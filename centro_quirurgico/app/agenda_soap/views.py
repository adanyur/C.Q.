from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#
from .models import Camas
from .serializers import CamasSerializer


@api_view(['GET'])
def camas_api_view(request):
    
    if request.method == 'GET':
        camas = Camas.objects.order_by('ch_codigo')
        camas_serializer = CamasSerializer(camas,many=True)
        return Response(camas_serializer.data,status=status.HTTP_200_OK)
