from django.db import models


# Create your models here.
class Estudiantes(models.Model):
    carnet = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField()
    creado = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('carnet',)


class Profesores(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length=50, blank=False)
    telefono = models.CharField(max_length=25, blank=True, default='')
    cellular = models.CharField(max_length=25, blank=True, default='')


class Materias(models.Model):
    materiacod = models.CharField(max_length=15, primary_key=True)
    descripcion = models.CharField(max_length=256)
    creditos = models.IntegerField(null=False, default=3)


class Periodos(models.Model):
    periodoid = models.IntegerField(primary_key=True, auto_created=True)
    descripcion = models.CharField(max_length=100, blank=False)
    anio = models.IntegerField(null=False)
    panual = models.IntegerField(null=False)
    meses = models.IntegerField(null=False, default=4)
    finicio = models.DateField(blank=False)
    ffin = models.DateField(blank=False)


class Sedes(models.Model):
    sedeid = models.IntegerField(primary_key=True, auto_created=True)
    descripcion = models.CharField(max_length=50, blank=False)


class Salones(models.Model):
    salonid = models.IntegerField(primary_key=True)
    sede = models.ForeignKey('Sedes')
    piso = models.IntegerField(null=False)


DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


TIPOS_HORA = (
    ('I', 'Inicio'),
    ('F', 'Fin')
)


class Horas(models.Model):
    horaid = models.IntegerField(primary_key=True, auto_created=True)
    hora = models.TimeField()
    tipo = models.CharField(choices=TIPOS_HORA, default='I', max_length=1, blank=False)


class Intervalo(models.Model):
    intervaloid = models.IntegerField(primary_key=True, auto_created=True)
    inicio = Horas()
    fin = Horas()


class Horarios(models.Model):
    horarioid = models.IntegerField(primary_key=True, auto_created=True)
    dia = models.IntegerField(choices=DAYS_OF_WEEK)
    hora = models.ManyToManyField(Intervalo)


class Oferta(models.Model):
    ofertaid = models.IntegerField(primary_key=True, auto_created=True)
    sede = models.ForeignKey('Sedes')
    periodo = models.ForeignKey('Periodos')
    grupo = models.ForeignKey('Grupos')


class Grupos(models.Model):
    grupoid = models.IntegerField(primary_key=True, auto_created=True)
    salon = models.ForeignKey('Salones')
    horario = models.ForeignKey('Horarios')
