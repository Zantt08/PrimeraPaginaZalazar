from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    pais_equipo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_equipo} - {self.pais_equipo}"

class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_locales") #Si se elimina el equipo, todos los partidos de ese equipo también
    equipo_visita = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_visita")
    goles_local = models.PositiveIntegerField()
    goles_visita = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.equipo_local} {self.goles_local} - {self.goles_visita} {self.equipo_visita}"

class Jugador(models.Model):
    POSICIONES = [
            ('ARQ', 'Arquero'),
            ('DEF', 'Defensor'),
            ('MED', 'Mediocampista'),
            ('DEL', 'Delantero'),
        ]

    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    posicion = models.CharField(max_length=3, choices=POSICIONES)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')

    def __str__(self):
        return f"{self.nombre} -> {self.get_posicion_display()}"
