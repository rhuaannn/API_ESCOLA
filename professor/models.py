from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        max_length=254, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name
