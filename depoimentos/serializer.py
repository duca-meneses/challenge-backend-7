from rest_framework import serializers
from depoimentos.models import Depoimentos

class DepoimentoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Depoimentos
        fields = '__all__'
