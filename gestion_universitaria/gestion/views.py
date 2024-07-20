from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estudiante, Carrera, Profesor, Inscripcion
from .forms import InscripcionForm
from django.contrib import messages


def index(request):
    return render(request, 'gestion/index.html')  # Asegúrate de que esta plantilla exista

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion/listar_estudiantes.html', {'estudiantes': estudiantes})

def listar_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'gestion/listar_carreras.html', {'carreras': carreras})

def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'gestion/listar_profesores.html', {'profesores': profesores})

def inscribir_estudiante(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Te has inscrito correctamente en la carrera!')
            return redirect('inscribir_estudiante')  # Redirige a la misma vista para mostrar el mensaje
    else:
        form = InscripcionForm()
    
    return render(request, 'gestion/inscripcion.html', {'form': form})
