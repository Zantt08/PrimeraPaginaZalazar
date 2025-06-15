from django.contrib import admin
from .models import Equipo, Jugador, Partido

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Partido)