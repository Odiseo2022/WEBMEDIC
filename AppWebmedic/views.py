from django.shortcuts import render
from django.http import HttpResponse
from AppWebmedic.models import *
from AppWebmedic.forms import formulario_consulta

# Create your views here.
def inicio(request):
    return render(request, "AppWebmedic/inicio.html")

def principal(request):
    return render(request, "AppWebmedic/padre.html")

def solicitud(request):
    return render(request, "AppWebmedic/solicitud.html")

def institucional(request):
    return render(request, "AppWebmedic/institucional.html")

def especialidad(request):
    return render(request, "AppWebmedic/especialidad.html")

def formulario_consulta(request):
    if request.method == "POST":
        paciente = Solicitante(request.POST['nombre_completo'], request.POST['email'])
        paciente.save()

    return render(request, "AppWebmedic/formulario_consulta.html")


  