from django.shortcuts import redirect, render
from . import forms

def first(request):
    return render(request, 'first.html')

def signup(request):
    form=forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        return render(request, 'login.html')
    else:
        form = forms.SignupForm(request.POST)
        return render(request, 'signup.html', {'form':form})


def login(request):
    return render(request, 'login.html')