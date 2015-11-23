# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('carnet', models.IntegerField(serialize=False, primary_key=True)),
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
            name='Intervalo',
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
            name='Oferta',
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
            ],
        ),
        migrations.AddField(
            model_name='salones',
            name='sede',
            field=models.ForeignKey(to='pfinalapi.Sedes'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='periodo',
            field=models.ForeignKey(to='pfinalapi.Periodos'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='sede',
            field=models.ForeignKey(to='pfinalapi.Sedes'),
        ),
        migrations.AddField(
            model_name='horarios',
            name='hora',
            field=models.ManyToManyField(to='pfinalapi.Intervalo'),
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
    ]
