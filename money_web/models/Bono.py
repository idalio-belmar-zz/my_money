# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from django.db import models
from money_web.models.Sueldo import Sueldo

class Bono(models.Model):
    sueldo      = models.ForeignKey(Sueldo)
    monto_bono  = models.IntegerField()
    fijo        = models.BooleanField()
    fecha       = models.DateField()
    
    def __unicode__(self):
        return self.bono

    class Meta:
        app_label = 'money_web'