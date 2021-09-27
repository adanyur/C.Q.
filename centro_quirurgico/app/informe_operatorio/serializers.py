from rest_framework import serializers
from .models import *


class InformeOperatorioSerializers(serializers.ModelSerializer):
    class Meta:
        model = InformeOperatorio
        fields = '__all__'
        extra_kwargs = {'id': {'validators': []},}


        