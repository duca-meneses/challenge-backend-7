from django.db import models

class Depoimentos(models.Model):
    nome = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='foto/%d/%m/%Y/', blank=True)
    depoimento = models.CharField(max_length=300)

    def __str__(self):
        return self.nome