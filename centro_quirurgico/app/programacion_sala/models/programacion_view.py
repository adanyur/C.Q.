from django.db import models


class IntervencionViewModel(models.Model):
    cq_codiqx = models.CharField(primary_key=True,max_length=6)
    cq_nomint = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'intervenciones_cq'
    
    def __str__(self):
        return self.cq_nomint


class CamasViewModel(models.Model):
    ch_codigo = models.CharField(primary_key=True,max_length=3)
    ch_descripcion = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'camas_hosp'
    
    def __str__(self):
        return self.ch_descripcion


class SalasViewModel(models.Model):
    sa_codsal =  models.CharField(primary_key=True,max_length=2)
    sa_nombre =  models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'salas'

    def __str__(self):
        return self.sa_nombre

class EspecialidadViewModel(models.Model):
    es_codigo = models.CharField(primary_key=True,max_length=3)
    es_descripcion = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'especialidades'

    def __str__(self):
        return self.es_descripcion



class ProgramacionViewModel(models.Model):
    cq_numope = models.CharField(primary_key=True,max_length=10)
    cq_fecha = models.DateTimeField()
    cq_hoinpr = models.DateTimeField()
    cq_hofipr = models.DateTimeField()
    cq_numhis = models.CharField(max_length=10)
    cq_paciente = models.CharField(max_length=100)
    cq_edad = models.CharField(max_length=2)

    se_codigo = models.ForeignKey(EspecialidadViewModel,on_delete=models.CASCADE,db_column='se_codigo')
    cq_codiqx = models.ForeignKey(IntervencionViewModel,on_delete=models.CASCADE,db_column='cq_codiqx')
    cq_codiqx2 = models.ForeignKey(IntervencionViewModel,on_delete=models.CASCADE,db_column='cq_codiqx2')
    cq_codiqx3 = models.ForeignKey(IntervencionViewModel,on_delete=models.CASCADE,db_column='cq_codiqx3')
    cq_cama = models.ForeignKey(CamasViewModel,on_delete=models.CASCADE,db_column='cq_cama')
    sa_codsal = models.ForeignKey(SalasViewModel,on_delete=models.CASCADE,db_column='sa_codsal')
    class Meta:
        managed = False
        db_table = 'programacion_cq'


class TipoDeParticipantesViewModel(models.Model):
    cq_codpar = models.CharField(primary_key=True,max_length=2)
    cq_despar = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'tipo_participantes_cq'

    def __str__(self):
        return self.cq_despar


class ProgramacionDetalleViewModel(models.Model):
    id = models.AutoField(primary_key=True)
    cq_numero = models.CharField(max_length=2)
    pl_codper = models.CharField(max_length=8)
    cq_codpar = models.ForeignKey(TipoDeParticipantesViewModel,on_delete=models.CASCADE, db_column='cq_codpar') 
    cq_numope = models.ForeignKey(ProgramacionViewModel,related_name='detalle',on_delete=models.CASCADE, db_column='cq_numope')
    class Meta:
        managed = False
        db_table = 'programacion_cq_d'
