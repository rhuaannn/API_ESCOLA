from rest_framework import generics
from professor.models import Professor
from professor.serializers import ProfessorSerializer


class ProfessorCreateListView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
