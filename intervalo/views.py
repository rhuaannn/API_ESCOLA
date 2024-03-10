from rest_framework import generics
from intervalo.models import Intervalo
from intervalo.serializers import IntervaloGetNameProfessorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class IntervaloCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloGetNameProfessorSerializer


class IntervaloRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,  GlobalDefaultPermission)
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloGetNameProfessorSerializer
