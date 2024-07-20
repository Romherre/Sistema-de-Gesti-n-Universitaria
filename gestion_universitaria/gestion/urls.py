from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('carreras/', views.listar_carreras, name='listar_carreras'),
    path('profesores/', views.listar_profesores, name='listar_profesores'),
    path('inscripcion/', views.inscribir_estudiante, name='inscribir_estudiante'),
]
