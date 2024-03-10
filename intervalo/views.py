from rest_framework import generics, status
from rest_framework.response import Response
from intervalo.models import Intervalo
from intervalo.serializers import IntervaloGetNameProfessorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class IntervaloCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloGetNameProfessorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IntervaloRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,  GlobalDefaultPermission)
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloGetNameProfessorSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
