from django import forms
from .models import Equipo, Jugador, Partido

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre_equipo', 'pais_equipo']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'edad', 'posicion', 'equipo']

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['equipo_local', 'equipo_visita', 'goles_local', 'goles_visita']

    def clean(self):
        cleaned_data = super().clean()
        equipo_local = cleaned_data.get('equipo_local')
        equipo_visita = cleaned_data.get('equipo_visita')

        if equipo_local == equipo_visita:
            raise forms.ValidationError("Un equipo no puede jugar contra sí mismo.")