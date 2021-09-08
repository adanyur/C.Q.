from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
#
from .models import ProgramacionSOAP
from .serializers import ProgramacionSOAPSerializer


@api_view(['GET'])
def soap_api_view(request,pk):
        if request.method == 'GET':                
            fecha = datetime.strptime(pk, "%Y-%m-%d").strftime("%d/%m/%Y")
            data = ProgramacionSOAP.objects.raw("SELECT * FROM cq_c_programacion('{0}')".format(fecha))

            if data : 
                ProgramacionSOAP_serializer = ProgramacionSOAPSerializer(data,many=True)
                return Response(ProgramacionSOAP_serializer.data)
            return Response({"message":"No hay programacion para la fecha seleccionada"})
