# Create your views here.

from rest_framework import generics
from rest_framework import filters
from tarea3.pfinalapi.models import Estudiante, Horarios
from tarea3.pfinalapi.serializers import EstudianteSerializer, HorariosSerializer
from rest_framework import permissions
from tarea3.pfinalapi.permissions import IsAdminUserOrReadOnly


class EstudianteList(generics.ListCreateAPIView,
                      generics.GenericAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = (permissions.AllowAny,)


class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView,
                        generics.GenericAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = (permissions.AllowAny,)


class HorariosList(generics.ListAPIView):
    serializer_class = HorariosSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Horarios.objects.all()
        estudiante = self.request.query_params.get('estudiante', None)
        if estudiante is not None:
            queryset = queryset.filter(estudiante=estudiante)
        return queryset



