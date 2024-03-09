from rest_framework import serializers
from auxiliar.models import Auxiliar


class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = "__all__"

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('O e-mail é obrigatório.')
        return value


class AuxiliiarGetNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = ['name']
