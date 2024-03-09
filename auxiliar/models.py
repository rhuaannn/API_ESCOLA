from django.db import models


class Auxiliar(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name