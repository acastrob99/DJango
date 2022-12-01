from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def bienvenido(request):
#     return HttpResponse("Hola mundo")

# def bienvenido(request):
#     return render(request,"bienvenido.html")

def bienvenido(request):
    mensajes = {"mensaje1": "valor_msg1", "mensaje2": "valor_msg2"}
    return render(request, "bienvenido.html",mensajes)

def despedida(request):
    return render(request, "despedida.html")


def listar_alumnos(request):
    listado_alumnos = [
        {"nombre":"nombre1","apellidos":"apellidos1","dni":"1111A"},
        {"nombre": "nombre2", "apellidos": "apellidos2", "dni": "2222B"},

    ]
    contexto = {"listado_alumnos": listado_alumnos}
    return render(request, "gestion/alumnos.html",contexto)


