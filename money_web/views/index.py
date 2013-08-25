# To change this template, choose Tools | Templates
# and open the template in the editor.
from django.http import HttpResponse
from django.template import RequestContext, loader
from money_web.models import Mes

def index(request):
    lista_meses = Mes.objects.order_by('id')
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'lista_meses': lista_meses,
    })
    return HttpResponse(template.render(context))
