from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import filters
# 
from .models import *
from .serializers import *

class HistoriaSearch(generics.ListAPIView):
    queryset = Historia.objects.all().filter(hc_estadoreg='1',hc_estado='00000001')
    serializer_class = HistoriaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['hc_numhis', 'hc_apepat','hc_apemat','hc_nombre','hc_sexo']


class Cie10Search(generics.ListAPIView):
    queryset = Cie10.objects.all()
    serializer_class = Cie10Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['codigo', 'descripcion']



@api_view(['GET'])
def historias_api_view(request,pk):
    if request.method == 'GET':
        queryset = Historia.objects.filter(hc_numhis=pk).first()
        historia_serializer = HistoriaSerializer(queryset)
        return Response(historia_serializer.data)
