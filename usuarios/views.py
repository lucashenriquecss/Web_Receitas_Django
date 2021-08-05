from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def cadastro(request): # metodo post para cadastrar usuarios
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():# verificação para evitar campos em branco ou com espaços
            print('O nome nao pode ser em branco!')
            return redirect('cadastro')
        if not email.strip():# verificação para evitar campos em branco ou com espaços
            print('O email nao pode ser em branco!')
            return redirect('cadastro')
        if senha != senha2:# verificação para evitar campos em branco ou com espaços
            print('O nome nao pode ser em branco!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuario ja cadastrado!')
            return redirect('cadastro') #verificando usuario se ja esta criado ou nao
        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save()
        print('Usuario cadastradii ciom sucesso')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST': # mesmo metodo de verificação do cadastro
        email = request.POST['email']
        senha = request.POST['senha']
        if email =="" or senha == "":# metedo para evitar que entre sem email e senha
            print('campos nao podem ficar em branco')
            return redirect('login')
        print(email,senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print("login realizado")      
                return redirect('dashboard')

    return render(request,'usuarios/login.html')


def logout(request):
    auth.logout(request)#saida do usuario
    return redirect('index')
    

def dashboard(request):
    #verificar se usuario esta logado
    if request.user.is_authenticated:      
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')

def criar_receita(request):
    return render(request, 'usuarios/criar_receita.html')