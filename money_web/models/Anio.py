# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from django.db import models

class Anio(models.Model):
    anio = models.CharField(max_length=4)
    
    def __unicode__(self):
        return self.anio
    
    class Meta:
        app_label = 'money_web'