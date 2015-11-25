# Create your views here.

from rest_framework import generics
from tarea3.pfinalapi.models import Estudiantes, Profesores, Periodos, Grupos, Materias, Sedes, Salones, Intervalos, \
    Horarios, Horas, Ofertas, GruposEstudiantes, ERegistro
from tarea3.pfinalapi.serializers import EstudiantesSerializer, ProfesoresSerializer, MateriasSerializer, \
    PeriodosSerializer, SedesSerializer, SalonesSerializer, HorasSerializer, IntervalosSerializer, \
    HorariosSerializer, OfertasSerializer, GruposSerializer, GruposEstudiantesSerializer, ERegistroSerializer
from rest_framework import permissions
from tarea3.pfinalapi.permissions import IsAdminUserOrReadOnly


class EstudiantesList(generics.ListCreateAPIView,
                      generics.GenericAPIView):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EstudiantesDetail(generics.RetrieveUpdateDestroyAPIView,
                        generics.GenericAPIView):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ERegistroList(generics.ListCreateAPIView,
                    generics.GenericAPIView):
    queryset = ERegistro.objects.all()
    serializer_class = ERegistroSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ERegistroDetail(generics.RetrieveUpdateDestroyAPIView,
                      generics.GenericAPIView):
    queryset = ERegistro.objects.all()
    serializer_class = ERegistroSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class ProfesoresList(generics.ListCreateAPIView, 
                     generics.GenericAPIView):
    queryset = Profesores.objects.all()
    serializer_class = ProfesoresSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProfesoresDetail(generics.RetrieveUpdateDestroyAPIView, 
                       generics.GenericAPIView):
    queryset = Profesores.objects.all()
    serializer_class = ProfesoresSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MateriasList(generics.ListCreateAPIView, 
                   generics.GenericAPIView):
    queryset = Materias.objects.all()
    serializer_class = MateriasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MateriasDetail(generics.RetrieveUpdateDestroyAPIView, 
                     generics.GenericAPIView):
    queryset = Materias.objects.all()
    serializer_class = MateriasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PeriodosList(generics.ListCreateAPIView, 
                   generics.GenericAPIView):
    queryset = Periodos.objects.all()
    serializer_class = PeriodosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PeriodosDetail(generics.RetrieveUpdateDestroyAPIView, 
                     generics.GenericAPIView):
    queryset = Periodos.objects.all()
    serializer_class = PeriodosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class SedesList(generics.ListCreateAPIView, 
                generics.GenericAPIView):
    queryset = Sedes.objects.all()
    serializer_class = SedesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SedesDetail(generics.RetrieveUpdateDestroyAPIView, 
                  generics.GenericAPIView):
    queryset = Sedes.objects.all()
    serializer_class = SedesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class SalonesList(generics.ListCreateAPIView, 
                  generics.GenericAPIView):
    queryset = Salones.objects.all()
    serializer_class = SalonesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SalonesDetail(generics.RetrieveUpdateDestroyAPIView, 
                    generics.GenericAPIView):
    queryset = Salones.objects.all()
    serializer_class = SalonesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class HorasList(generics.ListCreateAPIView, 
                generics.GenericAPIView):
    queryset = Horas.objects.all()
    serializer_class = HorasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HorasDetail(generics.RetrieveUpdateDestroyAPIView, 
                  generics.GenericAPIView):
    queryset = Horas.objects.all()
    serializer_class = HorasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class IntervalosList(generics.ListCreateAPIView, 
                     generics.GenericAPIView):
    queryset = Intervalos.objects.all()
    serializer_class = IntervalosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class IntervalosDetail(generics.RetrieveUpdateDestroyAPIView, 
                       generics.GenericAPIView):
    queryset = Intervalos.objects.all()
    serializer_class = IntervalosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class HorariosList(generics.ListCreateAPIView,
                   generics.GenericAPIView):
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class HorariosDetail(generics.RetrieveUpdateDestroyAPIView,
                     generics.GenericAPIView):
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class OfertasList(generics.ListCreateAPIView,
                  generics.GenericAPIView):
    queryset = Ofertas.objects.all()
    serializer_class = OfertasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OfertasDetail(generics.RetrieveUpdateDestroyAPIView,
                    generics.GenericAPIView):
    queryset = Ofertas.objects.all()
    serializer_class = OfertasSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class GruposList(generics.ListCreateAPIView,
                 generics.GenericAPIView):
    queryset = Grupos.objects.all()
    serializer_class = GruposSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GruposDetail(generics.RetrieveUpdateDestroyAPIView,
                   generics.GenericAPIView):
    queryset = Grupos.objects.all()
    serializer_class = GruposSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
class GruposEstudiantesList(generics.ListCreateAPIView,
                            generics.GenericAPIView):
    queryset = GruposEstudiantes.objects.all()
    serializer_class = GruposEstudiantesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GruposEstudiantesDetail(generics.RetrieveUpdateDestroyAPIView,
                              generics.GenericAPIView):
    queryset = GruposEstudiantes.objects.all()
    serializer_class = GruposEstudiantesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
