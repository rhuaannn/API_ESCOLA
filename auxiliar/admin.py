from django.contrib import admin
from auxiliar.models import Auxiliar


@admin.register(Auxiliar)
class AuxliarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
