# To change this template, choose Tools | Templates
# and open the template in the editor.
from my_money.money_web.models.Anio import Anio
from my_money.money_web.models.Mes import Mes
from my_money.money_web.models.Bono import Bono
from my_money.money_web.models.Gasto import Gasto
from my_money.money_web.models.Sueldo import Sueldo
from my_money.money_web.models.UserProfile import UserProfile

from django.contrib import admin

admin.site.register(Anio)
admin.site.register(Mes)
admin.site.register(Bono)
admin.site.register(Gasto)
admin.site.register(Sueldo)
admin.site.register(UserProfile)