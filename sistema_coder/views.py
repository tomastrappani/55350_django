#Funciones de controlador // controlador = view

from django.http import HttpResponse

from datetime import datetime
from django.shortcuts import render


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_fecha(request):
    hoy= datetime.now()
    saludo = f'Hola usuario, fecha: {hoy.day}/{hoy.month}'
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar_con_html(request):
    contexto = {
        "Profesor": "Pedro",
        "Tutores": ["Mariano","Ariel"],
        "Comision": 55350,
    }
    
    HttpResponse = render(
        request=request,
        template_name="base.html",
        context=contexto,
    )
    return HttpResponse

