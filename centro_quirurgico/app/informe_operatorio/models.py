from django.db import models

# Create your models here.

class InformeOperatorio(models.Model):
    cq_numope = models.CharField(primary_key=True,max_length=10)
    sa_codsal = models.CharField(max_length=2)
    cq_diag_procedimientos = models.CharField(max_length=400)
    cq_diag_hallazgos = models.CharField(max_length=400)
    cq_diag_complicaciones = models.CharField(max_length=400)
    cq_diag_pre_ope = models.CharField(max_length=200)
    cq_diag_pos_ope = models.CharField(max_length=200)
    cq_patolo = models.CharField(max_length=100)
    cq_diag_sang_aprox = models.CharField(max_length=10)
    cq_contgas = models.CharField(max_length=1)
    cq_fecpro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed=False
        db_table='informe_operatorio'