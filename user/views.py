
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
    return render(request, 'temp.html', context)

def login(request):
    return render(request, 'login.html')