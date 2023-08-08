from random import sample

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from depoimentos.models import Depoimento
from depoimentos.serializer import DepoimentoSerializer


class DepoimentoViewSet(viewsets.ModelViewSet):
    """Listando os depoimentos"""

    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer


class DepoimentoHomeView(APIView):
    """Lista 3 depoimentos aleatórios na rota /depoimentos-home"""

    def get(self, request):
        depoimentos = Depoimento.objects.all()
        num_depoimentos = depoimentos.count()

        if num_depoimentos < 3:
            return Response(
                {
                    'error': 'Não há depoimentos suficientes para retornar uma amostra com 3 depoimentos, Adicione mais depoimentos para usar esse endpoint corretamente'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        random_depoimentos = sample(list(depoimentos), 3)
        serializer = DepoimentoSerializer(random_depoimentos, many=True)
        return Response(serializer.data)
