from pessoas.models import Pessoa
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receitas
# Create your views here.
def cadastro(request): # metodo post para cadastrar usuarios
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):# verificação para evitar campos em branco ou com espaços
            messages.error(request, 'O nome não pode ficar em branco.')            
            return redirect('cadastro')

        if campo_vazio(email):# verificação para evitar campos em branco ou com espaços
            messages.error(request, ' O e-mail não pode ficar em branco')           
            return redirect('cadastro')

        if senha != senha2:# verificação para evitar campos em branco ou com espaços
            messages.error(request, 'As senhas não são iguais!') #mensagem de erro          
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Está conta ja existe, tente outra!')
            return redirect('cadastro') #verificando email se ja esta criado ou nao

        if User.objects.filter(username=nome).exists():
            messages.warning(request, 'Está conta ja existe, tente outra!')
            return redirect('cadastro') #verificando nome se ja esta criado ou nao

        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save()
        messages.success(request, 'Conta criada com sucesso!')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST': # mesmo metodo de verificação do cadastro
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):# metedo para evitar que entre sem email e senha
            messages.error(request, 'Os campos email e senha não podem ficar em branco.') 
            return redirect('login')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado!')      
                return redirect('dashboard')

    return render(request,'usuarios/login.html')


def logout(request):
    auth.logout(request)#saida do usuario
    return redirect('index')

def dashboard(request):
    #verificar se usuario esta logado
    if request.user.is_authenticated: 
        id = request.user.id#se o usuario for autenticado  pegue o id
        receitas= Receitas.objects.order_by('-data_receita').filter(
            pessoa=id #filtrando atraves do id do usuario
        )            
        return render(request, 'usuarios/dashboard.html',{'receitas':receitas})
    else:
        return redirect('index')

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
        return render(request, 'usuarios/criar_receita.html')

def campo_vazio(campo):
    return not campo.strip()
