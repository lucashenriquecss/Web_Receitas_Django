from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from receitas.models import Receitas
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    receitas = Receitas.objects.order_by('-data_receita').filter(publicada =True) 
    paginator = Paginator(receitas, 6)# Paginação, 3 receitas por pagina
    page = request.GET.get('page')
    receitas_por_paginas = paginator.get_page(page)
   
    dados = {
        'receitas' : receitas_por_paginas
    }
    return render(request,'receitas/index.html', dados)


def receita(request,receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)

    return render(request,'receitas/receita.html',{'receita':receita, })


def buscar(request):#metodo de busca
    lista_receitas = Receitas.objects.order_by('-data_receita').filter(publicada =True) 

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    


    return render(request, 'receitas/buscar.html', {'receitas': lista_receitas})


def criar_receita(request):

    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']

        user = get_object_or_404(User, pk=request.user.id) # passando o ID do usuario para variavel user      
        receita = Receitas.objects.create(
            pessoa=user, nome_receita=nome_receita,
            ingredientes=ingredientes, modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo, rendimento=rendimento,
            categoria=categoria, foto_receita=foto_receita
            )
        receita.save()
        return redirect('dashboard')
    else:       
        return render(request, 'receitas/criar_receita.html')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id) #buscando o id da receita para deletar
    receita.delete()
    return redirect('dashboard')


def editar_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)# Buscando a receita pelo id que queremos editar
    return render(request, 'receitas/editar_receita.html', {'receita':receita} )
    
def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        re = Receitas.objects.get(pk=receita_id)
        re.nome_receita = request.POST['nome_receita']
        re.ingredientes = request.POST['ingredientes']
        re.modo_preparo = request.POST['modo_preparo']
        re.tempo_preparo = request.POST['tempo_preparo']
        re.rendimento = request.POST['rendimento']
        re.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:#verificando se  tem alguma foto
            re.foto_receita = request.FILES['foto_receita']
        re.save()
    return redirect('dashboard')