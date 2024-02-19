#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def gamesView(request):
    context = {
       'message' : 'Hola, es una prueba que se esta realizando desde el contexto'
    }

    return render(request, 'games/index.html', context)




    


# Create your views here.