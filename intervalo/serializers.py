from rest_framework import serializers
from intervalo.models import Intervalo
from professor.serializers import ProfessorSerializerGetName


class IntervaloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervalo
        fields = '__all__'


class IntervaloGetNameProfessorSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializerGetName()

    class Meta:
        model = Intervalo
        fields = ['id', 'entrada', 'almoco',
                  'retorno_almoco', 'saida_expediente', 'descricao', 'professor']
