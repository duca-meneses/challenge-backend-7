from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from depoimentos.models import Depoimento


class TestStatusCode(APITestCase):
    def setUp(self):
        # Criando alguns objetos de teste para Depoimentos
        self.item1 = {
            'nome': 'Depoimento de Teste',
            'depoimento': 'Conteúdo do depoimento de teste',
        }
        self.depoimento1 = Depoimento.objects.create(
            nome='Depoimento 2', depoimento='Conteúdo do depoimento 2'
        )
        self.depoimento2 = Depoimento.objects.create(
            nome='Depoimento 3', depoimento='Conteúdo do depoimento 3'
        )
        self.depoimento3 = Depoimento.objects.create(
            nome='Depoimento 4', depoimento='Conteúdo do depoimento 4'
        )
        self.depoimento4 = Depoimento.objects.create(
            nome='Depoimento 5', depoimento='Conteúdo do depoimento 5'
        )

    def test_status_code_Get(self):
        """Testando a requisição Get do endpoint /depoimentos"""
        url = reverse('Depoimentos-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_code_Post(self):
        """Testando a requisição Post do endpoint /depoimentos"""
        url = reverse('Depoimentos-list')
        response = self.client.post(url, data=self.item1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_status_code_Put(self):
        """Testando a requisição Put do endpoint /depoimentos"""
        url = reverse('Depoimentos-detail', kwargs={'pk': self.depoimento1.pk})
        response = self.client.put(url, data=self.item1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_code_Delete(self):
        """Testando a requisição Delete do endpoint /depoimentos"""
        url = reverse('Depoimentos-detail', kwargs={'pk': self.depoimento2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
