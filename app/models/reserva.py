from django.db import models
from app.models.sala import Sala

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    horario = models.DateTimeField()