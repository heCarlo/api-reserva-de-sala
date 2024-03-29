from django.db import models

class Sala(models.Model):
    numero = models.IntegerField()
    capacidade = models.IntegerField()