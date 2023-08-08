from rest_framework import serializers

from depoimentos.models import Depoimento


class DepoimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depoimento
        fields = '__all__'
