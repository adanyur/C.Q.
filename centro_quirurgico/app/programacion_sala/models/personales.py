from django.db import models


class Personales(models.Model):
    pl_codper = models.CharField(max_length=3,primary_key=True) 
    pl_apepat = models.CharField(max_length=80)
    pl_apemat = models.CharField(max_length=80)
    pl_nombre = models.CharField(max_length=80)
    pl_estado = models.CharField(max_length=1)
    tipo = models.CharField(max_length=1,default='A')

    def nombre_personal(self):
         return  self.pl_apepat+" "+self.pl_apemat+" "+self.pl_nombre
         

    class Meta:
        db_table = 'personal'




class Medicos(models.Model):
    me_codigo  = models.CharField(max_length=3,primary_key=True)
    me_nombres = models.CharField(max_length=80)
    me_estado  = models.CharField(max_length=1)
    tipo = models.CharField(max_length=1,default='M')

    class Meta:
        managed=False
        db_table = 'medicos'


