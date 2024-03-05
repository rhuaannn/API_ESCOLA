from datetime import timedelta
from rest_framework import serializers
from intervalo.models import Intervalo
from professor.models import Professor
from professor.serializers import ProfessorSerializerGetName


class IntervaloGetNameProfessorSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializerGetName()

    class Meta:
        model = Intervalo
        fields = ['id', 'entrada', 'almoco',
                  'retorno_almoco', 'saida_expediente',
                  'descricao', 'professor_id', 'professor',]

    def create(self, validated_data):
        professor_data = validated_data.pop('professor')
        email = professor_data.get('email')

        if Professor.objects.filter(email=email).exists():
            raise serializers.ValidationError("Esse e-mail já está em uso!")
        professor_instance = Professor.objects.create(**professor_data)
        intervalo_instance = Intervalo.objects.create(
            professor=professor_instance, **validated_data)
        return intervalo_instance

    def validate(self, data):

        retorno_almoco = data['almoco'] + timedelta(minutes=60)

        if Intervalo.objects.filter(almoco=data['almoco']).exists():
            raise serializers.ValidationError(
                "Já existe um intervalo para este horário!")

        if Intervalo.objects.filter(retorno_almoco=retorno_almoco).exists():
            raise serializers.ValidationError(
                "Já existe um intervalo para este horário!")
        return data


class IntervaloSerializers(serializers.ModelSerializer):

    class Meta:
        model = Intervalo
        fields = '__all__'
