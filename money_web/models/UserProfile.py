# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#class Usuarios(models.Model):
    # This field is required.
    #user = models.OneToOneField(User)
    # Other fields here
    #rut = models.CharField(max_length=25
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    rut = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.rut
    
    class Meta:
        app_label = 'money_web'