from django.db import models

# Create your models here.

class Estudiante(models.Model):
    carnet = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField()
    creado = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('carnet',)

DAYS_OF_WEEK = (
    (0, 'Lunes'),
    (1, 'Martes'),
    (2, 'Miercoles'),
    (3, 'Jueves'),
    (4, 'Viernes'),
    (5, 'Sabado'),
    (6, 'Domingo'),
)


class Horarios(models.Model):
    estudiante = models.ForeignKey('Estudiante')
    codmateria = models.CharField(max_length=10, blank=False, null=False)
    materia  = models.CharField(max_length=50, blank=False, null=False)
    profesor = models.CharField(max_length=50, blank=False, null=False)
    sede = models.CharField(max_length=50, blank=False, null=False)
    aula = models.CharField(max_length=10, blank=False, null=False)
    dia = models.IntegerField(choices=DAYS_OF_WEEK)
    hora = models.TimeField()
    tiempo = models.IntegerField()
