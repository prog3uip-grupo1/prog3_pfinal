from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tarea3.pfinalapi import views

urlpatterns = patterns('tarea3.pfinalapi.views',
                       url(r'^estudiantes/$', views.EstudiantesList.as_view()),
                       url(r'^estudiantes/(?P<pk>[0-9]+)/$', views.EstudiantesDetail.as_view()),
                       url(r'^eregistro/$', views.ERegistroList.as_view()),
                       url(r'^eregistro/(?P<pk>[0-9]+)/$', views.ERegistroDetail.as_view()),
                       url(r'^profesores/$', views.ProfesoresList.as_view()),
                       url(r'^profesores/(?P<pk>[0-9]+)/$', views.ProfesoresDetail.as_view()),
                       url(r'^materias/$', views.MateriasList.as_view()),
                       url(r'^materias/(?P<pk>[0-9]+)/$', views.MateriasDetail.as_view()),
                       url(r'^periodos/$', views.PeriodosList.as_view()),
                       url(r'^periodos/(?P<pk>[0-9]+)/$', views.PeriodosDetail.as_view()),
                       url(r'^sedes/$', views.SedesList.as_view()),
                       url(r'^sedes/(?P<pk>[0-9]+)/$', views.SedesDetail.as_view()),
                       url(r'^salones/$', views.SalonesList.as_view()),
                       url(r'^salones/(?P<pk>[0-9]+)/$', views.SalonesDetail.as_view()),
                       url(r'^Horas/$', views.HorasList.as_view()),
                       url(r'^Horas/(?P<pk>[0-9]+)/$', views.HorasDetail.as_view()),
                       url(r'^intervalos/$', views.IntervalosList.as_view()),
                       url(r'^intervalos/(?P<pk>[0-9]+)/$', views.IntervalosDetail.as_view()),
                       url(r'^horarios/$', views.HorariosList.as_view()),
                       url(r'^horarios/(?P<pk>[0-9]+)/$', views.HorariosDetail.as_view()),
                       url(r'^ofertas/$', views.OfertasList.as_view()),
                       url(r'^ofertas/(?P<pk>[0-9]+)/$', views.OfertasDetail.as_view()),
                       url(r'^grupos/$', views.GruposList.as_view()),
                       url(r'^grupos/(?P<pk>[0-9]+)/$', views.GruposDetail.as_view()),
                       url(r'^gruposestudiantes/$', views.GruposEstudiantesList.as_view()),
                       url(r'^gruposestudiantes/(?P<pk>[0-9]+)/$', views.GruposEstudiantesDetail.as_view())
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
