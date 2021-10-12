from django.contrib.auth import authenticate, login, logout
from .models import User
from django.shortcuts import redirect, render
from .forms import UserCreationForm, AuthenticationForm


def index(request):
    return render(request, 'index.html')


def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'join.html', context)


def userlogin(request):
    context = {}
    user = request.user
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('kiwe')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def kiwe(request):
    if request.method == 'POST':
        return redirect('../q/1')
    return render(request, 'kiwe.html')

def friends(request):

    return render(request, 'friends.html')

def setting(request):
    if request.method == 'POST':
        setting = request.POST.get('setting')
        if setting == 'logout':
            logout(request)
            return redirect('/')
        elif setting == 'test':
            print('good')
    return render(request, 'setting.html')