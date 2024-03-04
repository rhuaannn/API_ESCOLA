from rest_framework import generics
from intervalo.models import Intervalo
from intervalo.serializers import IntervaloGetNameProfessorSerializer
from intervalo.serializers import IntervaloSerializer

class IntervaloCreateListView(generics.ListCreateAPIView):
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloGetNameProfessorSerializer


class IntervaloRetriveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloSerializer
