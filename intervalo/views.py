from rest_framework import generics, status
from rest_framework.response import Response
from datetime import timedelta
from intervalo.models import Intervalo
from intervalo.serializers import IntervaloGetNameProfessorSerializer


class IntervaloCreateListView(generics.ListCreateAPIView):
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloGetNameProfessorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IntervaloRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intervalo.objects.all()
    serializer_class = IntervaloGetNameProfessorSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Verifica se a descrição foi alterada
        if 'descricao' in serializer.validated_data:
            almoco = serializer.validated_data.get('almoco', instance.almoco)
            retorno_almoco = almoco + timedelta(minutes=60)
            # Verifica se há conflito com outros intervalos
            if Intervalo.objects.exclude(pk=instance.pk).filter(
                    almoco=almoco
            ).exists() or Intervalo.objects.exclude(pk=instance.pk).filter(
                    retorno_almoco=retorno_almoco
            ).exists():
                return Response(
                    {"detail": "Conflito de horários de almoço com outros intervalos."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        self.perform_update(serializer)
        return Response(serializer.data)
