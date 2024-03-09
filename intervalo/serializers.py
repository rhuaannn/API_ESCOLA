from rest_framework import serializers
from datetime import timedelta
from auxiliar.models import Auxiliar
from intervalo.models import Intervalo
from professor.models import Professor  # Importe o modelo Professor
from professor.serializers import ProfessorSerializerGetName
from auxiliar.serializers import AuxiliarSerializer, AuxiliiarGetNameSerializer
from datetime import timedelta
from rest_framework.response import Response


class IntervaloAuxiliarSerializer(serializers.ModelSerializer):
    auxiliar = AuxiliarSerializer()

    class Meta:
        model = Intervalo
        fields = ['id', 'entrada', 'almoco', 'retorno_almoco',
                  'saida_expediente', 'descricao', 'auxiliar']


class IntervaloGetNameProfessorSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializerGetName(required=False)
    auxiliar = AuxiliiarGetNameSerializer(required=False)
    
    class Meta:
        model = Intervalo
        fields = ['id', 'entrada', 'almoco', 'retorno_almoco',
                  'saida_expediente', 'descricao', 'professor', 'auxiliar']

    def create(self, validated_data):
        nome_professor = validated_data.get('professor', {}).get('name')
        nome_auxiliar = validated_data.get('auxiliar', {}).get('name')
        almoco_verification = validated_data['almoco']
        retorno_almoco_verification = validated_data['retorno_almoco']
        
        if nome_professor and nome_auxiliar:
            raise serializers.ValidationError(
                "Você só pode fornecer o nome de um professor ou de um auxiliar, não ambos."
            )
        elif nome_professor:
            try:
                professor = Professor.objects.get(name=nome_professor)
            except Professor.DoesNotExist:
                raise serializers.ValidationError(
                    "Professor com este nome não existe!"
                )
            validated_data['professor'] = professor
        elif nome_auxiliar:
            try:
                auxiliar = Auxiliar.objects.get(name=nome_auxiliar)
            except Auxiliar.DoesNotExist:
                raise serializers.ValidationError(
                    "Auxiliar com este nome não existe!"
                )
            validated_data['auxiliar'] = auxiliar
        else:
            raise serializers.ValidationError(
                "É necessário fornecer o nome do professor ou do auxiliar!"
            )

        if almoco_verification and retorno_almoco_verification:
            diferenca_almoco = retorno_almoco_verification - almoco_verification
            if diferenca_almoco < timedelta(minutes=60):
                raise serializers.ValidationError(
                    "O intervalo minimo de almoço é de uma hora.")

        if almoco_verification and retorno_almoco_verification and retorno_almoco_verification <= almoco_verification:
            raise serializers.ValidationError(
                "O horário de retorno do almoço deve ser depois da saida."
            )

        return super().create(validated_data)

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
        if almoco and retorno_almoco and retorno_almoco - almoco < timedelta(hours=1):
            raise serializers.ValidationError(
                "A diferença entre o horário de almoço e o horário de retorno do almoço deve ser de no máximo 60 minutos."
            )

        return data
