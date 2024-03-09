from django.db import models
from django.forms import ValidationError

from professor.models import Professor
from auxiliar.models import Auxiliar


class Intervalo(models.Model):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE,
        related_name='intervalos', null=True, blank=True)
    auxiliar = models.ForeignKey(
        Auxiliar, on_delete=models.CASCADE,
        related_name='intervalos', null=True, blank=True)

    entrada = models.DateTimeField()
    almoco = models.DateTimeField()
    retorno_almoco = models.DateTimeField()
    saida_expediente = models.DateTimeField()
    descricao = models.CharField(max_length=100, null=True, blank=True)

    def clean(self):
        if self.professor and self.auxiliar:
            raise ValidationError(
                "Você só pode especificar um Professor ou um Auxiliar, não ambos.")
        elif not self.professor and not self.auxiliar:
            raise ValidationError(
                "É necessário especificar um Professor ou um Auxiliar.")
