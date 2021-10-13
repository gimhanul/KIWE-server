from django.contrib.auth import authenticate, login, logout
from .models import User, FriendRequest
from django.shortcuts import redirect, render
from .forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

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

@login_required
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

@login_required
def send_friend_request(request, user_id):
    from_user = request.user
    to_user = User.objects.get(email = user_id)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user)


@login_required
def accept_friend_request(request, requestID):
    fr = FriendRequest.objects.get(id=requestID)
    if fr.to_user == request.user:
        fr.to_user.friends.add(fr.from_user)
        fr.from_user.friends.add(fr.to_user)
        fr.delete()

@login_required
def delete_friend_request(request, requestID):
    fr = FriendRequest.objects.get(id=requestID)
    if fr.to_user == request.user:
        fr.delete()