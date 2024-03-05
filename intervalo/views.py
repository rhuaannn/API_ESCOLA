from rest_framework import generics
from intervalo.models import Intervalo
from intervalo.serializers import IntervaloGetNameProfessorSerializer, IntervaloSerializers


class IntervaloCreateListView(generics.ListCreateAPIView):
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloGetNameProfessorSerializer


class IntervaloRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intervalo.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return IntervaloGetNameProfessorSerializer

        return IntervaloSerializers
