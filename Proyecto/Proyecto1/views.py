from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template,Context
def home_view(*args, **kwargs):
    doc_externo=open("Proyecto1/templates/saludo.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    pagina=plt.render(ctx)
    return HttpResponse(pagina)
def saludo(request):
    doc_externo=open("Proyecto1/templates/saludo.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    pagina=plt.render(ctx)
    return HttpResponse(pagina)
def despedida(request):

    return HttpResponse("Esta es una prueba de despedida")
