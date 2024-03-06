from rest_framework import serializers
from datetime import timedelta
from intervalo.models import Intervalo
from professor.serializers import ProfessorSerializerGetName


class IntervaloGetNameProfessorSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializerGetName()

    class Meta:
        model = Intervalo
        fields = ['id', 'entrada', 'almoco', 'retorno_almoco',
                  'saida_expediente', 'descricao', 'professor']

    def validate(self, data):
        almoco = data.get('almoco')
        retorno_almoco = data.get('retorno_almoco')

        # Verifica se o horário de retorno do almoço é após o horário de almoço
        if almoco and retorno_almoco and retorno_almoco <= almoco:
            raise serializers.ValidationError(
                "O horário de retorno do almoço deve ser após o horário de almoço.")

        # Verifica se a diferença entre o horário de almoço e o horário de retorno do almoço é menor ou igual a 60 minutos
        if almoco and retorno_almoco and retorno_almoco - almoco > timedelta(minutes=60):
            raise serializers.ValidationError(
                "A diferença entre o horário de almoço e o horário de retorno do almoço não pode exceder 60 minutos.")

        return data
