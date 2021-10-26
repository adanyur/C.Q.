from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# 
from .models import *
from .serializers import *

@api_view(['GET','POST'])
def incidencia_api_view(request):
    if request.method == 'GET':
        f419_data = F419Model.objects.all()
        f419_serializer = F419Serializer(f419_data,many=True)
        return Response(f419_serializer.data)

    if request.method == 'POST':
        f419_serializer = F419Serializer(data=request.data)
        if f419_serializer.is_valid():
            f419_serializer.save()
            return Response({'message':'Se registro correctamente!!'},status=status.HTTP_201_CREATED)
        return Response(f419_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def incidencia_detail_api_view(request,pk):
    f419_data = F419Model.objects.filter(id=pk).first()
    if f419_data:
        if request.method == 'GET':
            f419_serializer = F419Serializer(f419_data)
            return Response(f419_serializer.data)
        if request.method == 'PUT':
            f419_serializer = F419Serializer(f419_data,data = request.data)
            if f419_serializer.is_valid():
                f419_serializer.save()
                return Response({'message':'Se actualizo correctamente'})
            return Response(f419_serializer.errors)
    return Response({'message':'No se encontro dato'})
