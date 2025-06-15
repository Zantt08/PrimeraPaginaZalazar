from django.shortcuts import render, redirect
from .models import Equipo, Jugador, Partido
from .forms import EquipoForm, JugadorForm, PartidoForm

# Create your views here.

def inicio(request):
    return render(request, 'mainapp/inicio.html')

def equipos(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos')
    else:
        form = EquipoForm()

    equipos = Equipo.objects.all()

    return render(request, 'mainapp/equipos.html', {
        'form': form,
        'equipos': equipos,
    })

def jugadores(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugadores')
    else:
        form = JugadorForm()

    jugadores = Jugador.objects.all()

    return render(request, 'mainapp/jugadores.html', {
        'form': form,
        'jugadores': jugadores,
    })

def partidos(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partidos')
    else:
        form = PartidoForm()

    partidos = Partido.objects.all()

    return render(request, 'mainapp/partidos.html', {
        'form': form,
        'partidos': partidos,
    })