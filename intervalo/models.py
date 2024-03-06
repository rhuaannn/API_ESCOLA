from django.db import models

from professor.models import Professor


class Intervalo(models.Model):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE,
        related_name='professor', default=None)
    entrada = models.DateTimeField()
    almoco = models.DateTimeField()
    retorno_almoco = models.DateTimeField()
    saida_expediente = models.DateTimeField()
    descricao = models.CharField(max_length=100, null=True, blank=True,)

    def __str__(self):
        return self.descricao
