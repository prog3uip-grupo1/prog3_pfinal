# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
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
            name='Horarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codmateria', models.CharField(max_length=10)),
                ('materia', models.CharField(max_length=50)),
                ('profesor', models.CharField(max_length=50)),
                ('sede', models.CharField(max_length=50)),
                ('aula', models.CharField(max_length=10)),
                ('dia', models.IntegerField(choices=[(0, b'Lunes'), (1, b'Martes'), (2, b'Miercoles'), (3, b'Jueves'), (4, b'Viernes'), (5, b'Sabado'), (6, b'Domingo')])),
                ('hora', models.TimeField()),
                ('tiempo', models.IntegerField()),
                ('estudiante', models.ForeignKey(to='pfinalapi.Estudiante')),
            ],
        ),
    ]
