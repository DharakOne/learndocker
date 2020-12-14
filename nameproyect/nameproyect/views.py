from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template


def saludo(request):
    
    return HttpResponse("Hola alumnos esta es nuestra primera pagina con Django")

def cacular_Edad(request,age_of_birth):
    html="""
    <html><body>
    <h1>Tu edad es %s </h1><body></html>
    """ % age_of_birth
    return HttpResponse( html)

def saludo_plantilla(request,tu_nombre):
    plt=get_template("index.html")
    athlete_list=["Junior","Castro","Benjamin","Flores"]
    ctx={"tu_nombre":tu_nombre,"athlete_list":athlete_list,"section":"sitenews"}
    documento=plt.render(ctx)
    return HttpResponse(documento) 