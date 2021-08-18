from django.db.models import CharField, Value
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# 
from ..models.personales import *
from ..serializers.personales import *


@api_view(['GET'])
def personales_api_view(request):
    if request.method == 'GET':

        personales = Personales.objects.values_list('pl_codper','pl_nombre').annotate(tipo=Value('A',output_field=CharField())).filter(pl_estado='1')
        medicos = Medicos.objects.values_list('me_codigo','me_nombres').annotate(tipo=Value('M',output_field=CharField())).filter(me_estado='A')
        # medicos = Medicos.objects.annotate(tipo=Value('M',output_field=CharField())).filter(me_estado='A').values_list('me_codigo','me_nombres','tipo')

        data = personales.union(medicos)
        for x in data:            
            personal_serializer = PersonalSerializer(x,many=True)
            print(personal_serializer)
        # personal_serializer = PersonalSerializer(data,many=True) 
        # return Response(personal_serializer.data)
        return Response({'message':'test'})

