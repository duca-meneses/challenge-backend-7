from rest_framework import viewsets, status
from destinos.models import Destino
from destinos.serializer import DestinoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter
from rest_framework.response import Response


class DestinoFilter(FilterSet):
    nome = CharFilter(field_name='nome', lookup_expr='exact')
    class Meta:
        model = Destino
        fields = ['nome']

class DestinoViewSet(viewsets.ModelViewSet):
    """Listando os destinos"""
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DestinoFilter

    def list(self, request, *args, **kwargs):
        # Verificar se o parâmetro 'nome' foi fornecido na URL
        nome = request.query_params.get('nome')
        if nome is None:
            return super().list(request, *args, **kwargs)
        return Response({"mensagem": "Nenhum destino foi encontrado"}, status=status.HTTP_400_BAD_REQUEST)
        
    

    

    

