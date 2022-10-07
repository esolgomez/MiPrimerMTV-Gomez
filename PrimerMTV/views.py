from datetime import datetime
from re import template
from unittest import loader
from django.http import HttpResponse
from django.template import  loader
from datetime import datetime
import random
from Home.models import Familiar


def crear_familiar(request, nombre, apellido):
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())

    familiar.save()

    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({})   
    return HttpResponse(template_renderizado)
    

def mi_familia(request):
    familiares = Familiar.objects.all()
    template = loader.get_template('mi_familia.html')
    template_renderizado = template.render({'familiares': familiares})
    return HttpResponse(template_renderizado)