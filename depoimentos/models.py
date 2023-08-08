import os
import random
import string

from django.db import models


def gerar_codigo_aleatorio():
    # Gera uma sequência de três números aleatórios
    return ''.join(random.choices(string.ascii_letters + string.digits, k=3))


def declarador_directory_path(instance, filename):
    # Gera o caminho para a pasta de depoimento da foto com base no nome do Declarador e no código aleatório
    nome_pasta = instance.nome + gerar_codigo_aleatorio()
    return os.path.join('foto/depoimentos', nome_pasta, filename)


class Depoimento(models.Model):
    nome = models.CharField(max_length=30)
    foto = models.ImageField(upload_to=declarador_directory_path, blank=True)
    depoimento = models.CharField(max_length=300)

    def __str__(self):
        return self.nome
