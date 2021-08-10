from django.db import models


class DisponibilidadSalas(models.Model):
    id = models.IntegerField(primary_key=True)
    hora = models.TimeField()
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField()