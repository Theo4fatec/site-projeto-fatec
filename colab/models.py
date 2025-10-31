from django.db import models


class Teste(models.Model):
    categoria = models.CharField(max_length=255)
    quantidade = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.categoria}: {self.quantidade}'