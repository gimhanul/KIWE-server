
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from .forms import UserCreationForm


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


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
    else:
        return render(request,'login.html')


def main(request):
    return render(request, 'main.html')