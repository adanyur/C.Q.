from django.db import models

# Create your models here.
class F419Model(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    historia = models.CharField(max_length=10)
    glosa = models.TextField()
    turno = models.CharField(max_length=1)
    usuario = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario_actualizado = models.CharField(max_length=50,null=True, blank=True)
    fecha_actualizado = models.DateTimeField(null=True, blank=True)
    class Meta:
        managed =False
        db_table ='incidencia'


class F419DetailModel(models.Model):
    tipo = models.CharField(max_length=2)
    value = models.CharField(max_length=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=50)
    id_cabecera = models.ForeignKey(F419Model,related_name='detalles',on_delete=models.CASCADE,db_column='id_cabecera',null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'incidencia_d'