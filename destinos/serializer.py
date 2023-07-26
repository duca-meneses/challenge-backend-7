from rest_framework import serializers
from destinos.models import Destino

class DestinoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destino
        fields = '__all__'