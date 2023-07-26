from rest_framework import viewsets, generics
from destinos.models import Destino
from destinos.serializer import DestinoSerializer

class DestinoViewSet(viewsets.ModelViewSet):
    """Listando os destinos"""
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer

    

