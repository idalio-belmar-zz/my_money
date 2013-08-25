# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from django.db import models
from money_web.models.Mes import Mes

class Gasto(models.Model):
    mes         = models.ForeignKey(Mes)
    monto_gasto = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    fijo        = models.BooleanField()
    
    def __unicode__(self):
        return self.descripcion    

    class Meta:
        app_label = 'money_web'