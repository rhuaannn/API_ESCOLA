from rest_framework import serializers
from datetime import timedelta
from intervalo.models import Intervalo
from professor.models import Professor  # Importe o modelo Professor
from professor.serializers import ProfessorSerializerGetName
from datetime import timedelta
from rest_framework.response import Response


class IntervaloGetNameProfessorSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializerGetName()

    class Meta:
        model = Intervalo
        fields = ['id', 'entrada', 'almoco', 'retorno_almoco',
                  'saida_expediente', 'descricao', 'professor']

    def create(self, validated_data):
        nome_professor = validated_data.pop('professor').get('name')

        if not nome_professor:
            raise serializers.ValidationError(
                "Nome do professor não fornecido!")

        try:
            professor = Professor.objects.get(name=nome_professor)
        except Professor.DoesNotExist:
            raise serializers.ValidationError(
                "É necessário criar um professor!")

        intervalo = Intervalo.objects.create(
            professor=professor, **validated_data)

        return intervalo
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Verifica se a descrição foi alterada
        if 'descricao' in serializer.validated_data:
            almoco = serializer.validated_data.get('almoco', instance.almoco)
            retorno_almoco = almoco + timedelta(minutes=60)
            # Verifica se há conflito com outros intervalos
            if (
                Intervalo.objects.filter(~Q(pk=instance.pk))
                .filter(
                    Q(almoco=almoco) | Q(retorno_almoco=retorno_almoco)
                )
                .exists()
            ):
                return Response(
                    {"detail": "Conflito de horários de almoço com outros intervalos."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        self.perform_update(serializer)
        return Response(serializer.data)
    
    def validate(self, data):
        almoco = data.get('almoco')
        retorno_almoco = data.get('retorno_almoco')

        # Verifica se o horário de retorno do almoço é após o horário de almoço
        if almoco and retorno_almoco and retorno_almoco <= almoco:
            raise serializers.ValidationError(
                "O horário de retorno do almoço deve ser após o horário de almoço."
            )

        # Verifica se a diferença entre o horário de almoço e o horário de retorno do almoço é menor ou igual a 60 minutos
        if almoco and retorno_almoco and retorno_almoco - almoco > timedelta(minutes=60):
            raise serializers.ValidationError(
                "A diferença entre o horário de almoço e o horário de retorno do almoço deve ser de no máximo 60 minutos."
            )

        return data
