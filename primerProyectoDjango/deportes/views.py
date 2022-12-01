from django.shortcuts import render

# Create your views here.

def deportes(request):
    mensajes = {"titulo": "titulo deportes", "descripcion": "¡descripcion_deportes"}
    return render(request, "inicio.html",mensajes)

def selecciones_mundial(request):
    listado_selecciones = [
        {"seleccion": "españa", "continente": "europa", "mundiales_ganados": 1},
        {"seleccion": "brasil", "continente": "america", "mundiales_ganados": 5 },
        {"seleccion": "argentina", "continente": "america", "mundiales_ganados": 2},
    ]
    contexto = {"selecciones": listado_selecciones}
    return render(request, "selecciones.html", contexto)

def aniadir_seleccion(request):
    espania = {"nombre": "España", "continente": "Europa", "num_mundiales": 1}
    brasil = {"nombre": "Brasil", "continente": "America", "num_mundiales": 5}
    francia = {"nombre": "Francia", "continente": "Europa", "num_mundiales": 2}
    senegal = {"nombre": "Senegal", "continente": "Africa", "num_mundiales": 0}

    lista_selecciones = [espania, brasil, francia, senegal]
    listado_continentes = ["Europa", "America", "Asia", "Africa", "Oceania"]

    if request.method == 'POST':
        nom_seleccion = request.POST['seleccion']
        nom_continente = request.POST['continente']
        mundiales_ganados = request.POST['mundiales_ganados']

        new_seleccion = {"nombre": nom_seleccion, "continente": nom_continente, "num_mundiales": mundiales_ganados}

        lista_selecciones.append(new_seleccion)

    contexto = {"listado_selecciones": lista_selecciones, "listado_contienentes" :listado_continentes}

    return render(request, "aniadir_seleccion.html",contexto)

