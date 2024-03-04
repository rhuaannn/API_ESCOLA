from django.contrib import admin

from intervalo.models import Intervalo


@admin.register(Intervalo)
class IntervalorAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'entrada', 'saida_expediente',
                    'retorno_almoco', 'almoco', 'professor')
