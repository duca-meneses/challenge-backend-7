from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from destinos.models import Destino

class Test_status_code(APITestCase):
    def setUp(self):
        # Criando alguns objetos de teste para Destinos
        self.item1 = {'nome': 'Destino de Teste', 'foto_1': '', 'foto_2': '', 'meta_descricao': 'test_descrição', 'texto_descritivo':''}
        self.destino1 = Destino.objects.create(nome='Destino 2', foto_1='', foto_2='', meta_descricao='descrição',texto_descritivo='test')
        self.destino2 = Destino.objects.create(nome='Destino 3', foto_1='', foto_2='',meta_descricao='descrição',texto_descritivo='test')

    def test_status_code_GET(self):
        """Testando a requisição GET do endpoint /destinos"""
        url = reverse('Destinos-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_status_code_POST(self):
        """Testando a requisição POST do endpoint /destinos"""
        url = reverse('Destinos-list')
        response = self.client.post(url, data=self.item1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_status_code_PUT(self):
        """Testando a requisição PUT do endpoint /destinos"""
        url = reverse('Destinos-detail', kwargs={'pk': self.destino1.pk})
        response = self.client.put(url,data=self.item1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_code_DELETE(self):
        """Testando a requisição DELETE do endpoint /destinos"""
        url = reverse('Destinos-detail', kwargs={'pk': self.destino1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)