from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tarea3.pfinalapi import views

urlpatterns = patterns('tarea3.pfinalapi.views',
                       url(r'^estudiante/$', views.EstudianteList.as_view()),
                       url(r'^estudiante/(?P<pk>[0-9]+)/$', views.EstudianteDetail.as_view()),
                       url(r'^horarios/$', views.HorariosList.as_view())
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
