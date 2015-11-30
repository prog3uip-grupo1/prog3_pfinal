from rest_framework import serializers
from tarea3.pfinalapi.models import Estudiantes, Profesores, Periodos, Grupos, Materias, Sedes, Salones, Intervalos, \
    Horarios, Horas, Ofertas, GruposEstudiantes, ERegistro, UserProfile
from rest_auth.serializers import UserDetailsSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile


class UserSerializer(UserDetailsSerializer):

    carnet = serializers.CharField(source="userprofile.carnet")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('carnet',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        carnet = profile_data.get('carnet')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data and carnet:
            profile.carnet = carnet
            profile.save()
        return instance


class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ('carnet', 'nombre', 'apellido', 'email', 'creado')


class ERegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ERegistro
        fields = ('estudiante', 'usuario', 'creado')
        

class ProfesoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesores
        fields = ('id', 'nombre', 'apellido', 'telefono', 'celular')


class MateriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materias
        fields = ('materiacod', 'descripcion', 'creditos')


class PeriodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodos
        fields = ('periodoid', 'descripcion', 'anio', 'panual', 'meses', 'finicio', 'ffin')


class SedesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sedes
        fields = ('sedeid', 'descripcion', 'direccion', 'telefono')


class SalonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salones
        fields = ('salonid', 'sede', 'piso')


class HorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horas
        fields = ('horaid', 'hora', 'tipo')


class IntervalosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervalos
        fields = ('intervaloid', 'inicio', 'fin')


class HorariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horarios
        fields = ('horarioid', 'dia', 'hora')


class OfertasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ofertas
        fields = ('ofertaid', 'sede', 'periodo', 'grupo')


class GruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupos
        fields = ('grupoid', 'salon', 'horario')


class GruposEstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GruposEstudiantes
        fields = ('grupoid', 'estudiantes')

