from rest_framework import generics
from auxiliar.models import Auxiliar
from auxiliar.serializers import AuxiliarSerializer


class AuxiliarCreateListView(generics.ListCreateAPIView):
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer


class AuxiliarRetriveUpdateDestroyView(generics.RetrieveUpdateAPIView):
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer