from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Receitas
# Create your views here.


def index(request):
    receitas = Receitas.objects.order_by('-data_receita').filter(publicada =True) 
   
    return render(request,'index.html', {'receitas': receitas})


def receita(request,receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    return render(request,'receita.html',{'receita':receita, })


def buscar(request):#metodo de busca
    lista_receitas = Receitas.objects.order_by('-data_receita').filter(publicada =True) 

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    


    return render(request, 'buscar.html', {'receitas': lista_receitas})