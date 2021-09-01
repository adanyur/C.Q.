from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# 
from ..models.intervencion import *
from ..serializers.intervencion import *


@api_view(['GET'])
def intervencion_api_view(request,pk):
     if request.method == 'GET':
         intervencions = Intervencion.objects.all().filter(se_codigo=pk)
         Intervencion_serializers = IntervencionSerializers(intervencions,many=True)
         return Response(Intervencion_serializers.data)
