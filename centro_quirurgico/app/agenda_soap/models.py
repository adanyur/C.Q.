from django.db import models

# Create your models here.

class ProgramacionSOAP(models.Model):
    cq_numope = models.CharField(max_length=10,primary_key=True)
    diahora = models.CharField(max_length=50)
    sala = models.CharField(max_length=2)
    paciente = models.CharField(max_length=100)
    intervencion= models.CharField(max_length=50)
    cirujano = models.CharField(max_length=80)
    anestesia = models.CharField(max_length=30)
    cama = models.CharField(max_length=6)
    pedido = models.CharField(max_length=199)
    cq_fecha = models.CharField(max_length=80)
    cq_hoinpr = models.DateTimeField()
    cq_hofipr = models.DateTimeField()
    cq_hoinej =models.DateTimeField()
    cq_hofiej = models.DateTimeField()
    cq_numhis = models.CharField(max_length=10)
    cq_estado = models.CharField(max_length=1)
    edad = models.IntegerField()
    semanas = models.CharField(max_length=10)
    tiempo = models.IntegerField()
    inf_ope = models.BooleanField()
    cq_indrep = models.CharField(max_length=1)