from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
#
from ..models.personales import *
from ..serializers.programacion_cq import *


@api_view(['POST'])
def programacion_cq_api_view(request):
    if request.method == 'POST':
        serializer = ProgramacionCQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)