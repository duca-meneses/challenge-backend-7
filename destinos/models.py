import os

from django.db import models


def destino_directory_path(instance, filename):
    # Gera o caminho para a pasta de destino da foto com base no nome do Destino
    return os.path.join('foto/destinos', instance.nome, filename)


class Destino(models.Model):
    nome = models.CharField(max_length=30)
    foto_1 = models.ImageField(upload_to=destino_directory_path, blank=True)
    foto_2 = models.ImageField(upload_to=destino_directory_path, blank=True)
    meta_descricao = models.CharField(max_length=160, null=True)
    texto_descritivo = models.CharField(max_length=300, blank=True)

    def __str__(self) -> str:
        return self.nome
