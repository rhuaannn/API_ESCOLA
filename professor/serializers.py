from rest_framework import serializers
from professor.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("E-mail é um campo obrigatório!")
        return value


class ProfessorSerializerGetName(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['name',]
