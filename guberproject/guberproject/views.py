from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from gestionUsuarios.models import *

def index(request): #Index guber.com
    template = loader.get_template('index.html')
    template_index = template.render()
    return HttpResponse(template_index)

def loggin(request):
    template = loader.get_template('index.html')
    template_index = template.render()
    rol = str(request.POST["rol"])
    user = str(request.POST["user"])
    pw = str(request.POST["pw"])
    d = chef.objects.filter(user=user, pw=pw)
    if(len(d)>=1):
        template = loader.get_template('chef_section_pedidos.html')
        datos = {"nombre":d[0].nombre,
                "edad":d[0].edad, 
                "tarjeta_profesional":d[0].tarjeta_profesiona,
                "correo":d[0].correo,
                "direccion":d[0].direccion,
                "pedidos":[1,2,3,4,5,6,7,8,9,10,11,12]}
        

        template_index = template.render(datos)
        return HttpResponse(template_index) 
    else:
        return HttpResponse(template_index)  
    print(len(d))

def chef_pedidos(request):
    template = loader.get_template('chef_pedidos.html')
    template_index = template.render()
    return HttpResponse(template_index)

        