from django.contrib import admin
from .models import Estudiante, Carrera, Profesor

admin.site.register(Estudiante)
admin.site.register(Carrera)
admin.site.register(Profesor)