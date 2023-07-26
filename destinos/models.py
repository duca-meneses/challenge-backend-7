from django.db import models

class Destino(models.Model):
    nome = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='foto/destinos', blank=True)
    preco = models.FloatField(max_length=10)

    def __str__(self) -> str:
            return self.nome
