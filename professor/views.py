from rest_framework import generics
from professor.models import Professor
from professor.serializers import ProfessorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class ProfessorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
