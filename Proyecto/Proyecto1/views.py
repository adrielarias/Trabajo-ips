from django.http import HttpResponse

def saludo(request):
    pagina="""
<HEAD>
<TITLE>saludo</TITLE>
</HEAD>
<BODY>
prueba saludo
</BODY>
</HTML>
    """
    return HttpResponse(pagina)
def despedida(request):

    return HttpResponse("Esta es una prueba de despedida")
