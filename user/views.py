
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from . import forms


def first(request):
    return render(request, 'first.html')

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
    return render(request, 'temp.html', context)

def login(request):
    return render(request, 'login.html')