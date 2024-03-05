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
                  'descricao','professor',]

    def create(self, validated_data):
        professor_data = validated_data.pop('professor')
        email = professor_data.get('email')

        if Professor.objects.filter(email=email).exists():
            raise serializers.ValidationError("Esse e-mail já está em uso!")
        professor_instance = Professor.objects.create(**professor_data)
        intervalo_instance = Intervalo.objects.create(
            professor=professor_instance, **validated_data)
        return intervalo_instance

    def update(self, instance, validated_data):
        professor_data = validated_data.pop('professor')
        name = professor_data.get('name')

        if Professor.objects.filter(name=name).exists():
            professor_instance = Professor.objects.get(name=name)
            for attr, value in professor_data.items():
                setattr(professor_instance, attr, value)
            professor_instance.save()
            print(professor_instance)
        else:
            raise serializers.ValidationError(
                "Professor não cadastrado! ")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save() 

        return instance

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
