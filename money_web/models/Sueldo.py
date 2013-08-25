# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from django.db import models
from money_web.models.UserProfile import UserProfile

class Sueldo(models.Model):
    usuario      = models.ForeignKey(UserProfile)
    monto_sueldo = models.IntegerField()
    descripcion  = models.CharField(max_length=200)
    empresa      = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.empresa

    class Meta:
        app_label = 'money_web'