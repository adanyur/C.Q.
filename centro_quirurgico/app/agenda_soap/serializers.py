from rest_framework import serializers
from .models import ProgramacionSOAP

class ProgramacionSOAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramacionSOAP
        fields = '__all__'
        read_only_fields = fields