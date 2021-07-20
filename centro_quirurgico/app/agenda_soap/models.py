from django.db import models

# Create your models here.

class Camas(models.Model):
    ch_codigo = models.CharField(primary_key=True,max_length=3)
    ch_numcam = models.CharField(max_length=4)
    ch_numhab = models.CharField(max_length=3)
    ch_descripcion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'camas_hosp'
