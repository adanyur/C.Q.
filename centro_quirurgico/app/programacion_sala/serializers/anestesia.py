from rest_framework import serializers
from ..models.anestesia import *

class AnestesiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anestesia
        fields = ('hora','descripcion','estado')
        read_only_fields = fields