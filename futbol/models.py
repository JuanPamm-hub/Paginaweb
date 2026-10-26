from django.db import models


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    dorsal = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} (#{self.dorsal})"
