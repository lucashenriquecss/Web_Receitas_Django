from django.shortcuts import redirect, render

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
           
        print(nome,email,senha,senha2)
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    return render(request,'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    pass

