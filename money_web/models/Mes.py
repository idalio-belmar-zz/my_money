# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from django.db import models
from money_web.models.Anio import Anio

class Mes(models.Model):
    anio = models.ForeignKey(Anio)
    mes     = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.mes
    
    
    class Meta:
        app_label = 'money_web'