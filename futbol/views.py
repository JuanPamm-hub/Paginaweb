from django.shortcuts import render
from .models import Jugador


def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futbol/index.html', {'jugadores': jugadores})
