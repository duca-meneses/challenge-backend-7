from random import sample
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response
from depoimentos.models import Depoimento
from depoimentos.serializer import DepoimentoSerializer


class DepoimentoViewSet(viewsets.ModelViewSet):
    """Listando os depoimentos """
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer


class DepoimentoHomeView(APIView):
    def get(self, request):
        depoimentos = Depoimento.objects.all()
        random_depoimentos = sample(list(depoimentos), 3)
        serializer = DepoimentoSerializer(random_depoimentos, many=True)
        return Response(serializer.data)

