from rest_framework import serializers
from tarea3.pfinalapi.models import Estudiante, Horarios


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('carnet', 'nombre', 'apellido', 'email', 'creado')


class HorariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horarios
        fields = ('estudiante', 'codmateria', 'materia', 'sede', 'aula', 'dia', 'hora', 'tiempo')
        

