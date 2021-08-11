from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# 
from ..models.personales import *
from ..serializers.personales import *


@api_view(['GET'])
def personales_api_view(request):
    if request.method == 'GET':
        personales = Personales.objects.all().values_list('pl_codper','pl_nombre','tipo').filter(pl_estado='1')
        medicos = Medicos.objects.all().values_list('me_codigo','me_nombres','tipo').filter(me_estado='A')



        # personal_serializer = PersonalSerializer(personales,many=True)
        # medicos_serializers = MedicosSerializers(medicos,many=True)

        data = personales.union(medicos)
        print(data)
        return Response({'message':'test'})
        
        
        # return Response(personal_serializer.data)
        # medicos = Medicos.objects.all().filter(me_estado='A')
        
        # return Response(medicos_serializers.data)

