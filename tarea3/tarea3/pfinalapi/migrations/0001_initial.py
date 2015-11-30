# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ERegistro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('carnet', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('creado', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('carnet',),
            },
        ),
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('grupoid', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='GruposEstudiantes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estudiante', models.ForeignKey(to='pfinalapi.Estudiantes')),
                ('grupoid', models.OneToOneField(to='pfinalapi.Grupos')),
            ],
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('horarioid', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.IntegerField(choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b'Sunday')])),
            ],
        ),
        migrations.CreateModel(
            name='Horas',
            fields=[
                ('horaid', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('hora', models.TimeField()),
                ('tipo', models.CharField(default=b'I', max_length=1, choices=[(b'I', b'Inicio'), (b'F', b'Fin')])),
            ],
        ),
        migrations.CreateModel(
            name='Intervalos',
            fields=[
                ('intervaloid', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('materiacod', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=256)),
                ('creditos', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Ofertas',
            fields=[
                ('ofertaid', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.ForeignKey(to='pfinalapi.Grupos')),
            ],
        ),
        migrations.CreateModel(
            name='Periodos',
            fields=[
                ('periodoid', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('panual', models.IntegerField()),
                ('meses', models.IntegerField(default=4)),
                ('finicio', models.DateField()),
                ('ffin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(default=b'', max_length=25, blank=True)),
                ('cellular', models.CharField(default=b'', max_length=25, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salones',
            fields=[
                ('salonid', models.IntegerField(serialize=False, primary_key=True)),
                ('piso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sedes',
            fields=[
                ('sedeid', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=256)),
                ('telefono', models.CharField(default=b'', max_length=25, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carnet', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='salones',
            name='sede',
            field=models.ForeignKey(to='pfinalapi.Sedes'),
        ),
        migrations.AddField(
            model_name='ofertas',
            name='periodo',
            field=models.ForeignKey(to='pfinalapi.Periodos'),
        ),
        migrations.AddField(
            model_name='ofertas',
            name='sede',
            field=models.ForeignKey(to='pfinalapi.Sedes'),
        ),
        migrations.AddField(
            model_name='horarios',
            name='hora',
            field=models.ManyToManyField(to='pfinalapi.Intervalos'),
        ),
        migrations.AddField(
            model_name='grupos',
            name='horario',
            field=models.ForeignKey(to='pfinalapi.Horarios'),
        ),
        migrations.AddField(
            model_name='grupos',
            name='salon',
            field=models.ForeignKey(to='pfinalapi.Salones'),
        ),
        migrations.AddField(
            model_name='eregistro',
            name='estudiante',
            field=models.OneToOneField(to='pfinalapi.Estudiantes'),
        ),
        migrations.AddField(
            model_name='eregistro',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
