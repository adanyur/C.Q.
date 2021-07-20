from django.db import models

# Create your models here.

class ProgramacionSOAP(models.Model):
    cq_numope = models.CharField(max_length=10,primary_key=True)
    diahora = models.CharField(max_length=50)
    sala = models.CharField(max_length=2)
    paciente = models.CharField(max_length=100)
    intervencion= models.CharField(max_length=50)
