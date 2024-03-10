from rest_framework import generics
from auxiliar.models import Auxiliar
from auxiliar.serializers import AuxiliarSerializer

from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class AuxiliarCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer


class AuxiliarRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer
