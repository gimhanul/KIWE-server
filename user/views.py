from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http.response import HttpResponse
from .models import User, FriendRequest, Profile
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserCreationForm, AuthenticationForm, ProfileForm
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
            if not Profile.objects.filter(user=request.user).exists():
                return redirect('../profileCreate/')
            else:
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
    temp = User.objects.get(id=request.user.id).friends.values('profile')
    temp = [i['profile'] for i in temp]
    friends = []
    for i in temp:
        temp1 = Profile.objects.filter(id=i).values('name', 'description', 'image')[0]
        friends.append(temp1)

    
    context = {
        'friends': friends
    }
    return render(request, 'friends.html', context)

def setting(request):
    if request.method == 'POST':
        setting = request.POST.get('setting')
        if setting == 'logout':
            logout(request)
            return redirect('/')
        elif setting == 'profile':
            print(".")
    return render(request, 'setting.html')

@login_required
def send_friend_request(request, user_id):
    from_user = request.user
    to_user = User.objects.get(id = user_id)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')
        


@login_required
def accept_friend_request(request, requestID):
    fr = FriendRequest.objects.get(id=requestID)
    if fr.to_user == request.user:
        fr.to_user.friends.add(fr.from_user)
        fr.from_user.friends.add(fr.to_user)
        fr.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')

@login_required
def delete_friend_request(request, requestID):
    fr = FriendRequest.objects.get(id=requestID)
    if fr.to_user == request.user:
        fr.delete()
        return HttpResponse('friend request deleted')
    else:
        return HttpResponse('friend request deleted')

def profile(request):
    return render(request, 'profile.html')

def profileCreate(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.image = request.FILES.get('image')
            profile.user = request.user
            profile.save()
            return redirect('kiwe')
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'profileCreate.html', context)

def profileEdit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            lastUser = request.user.profile
            #lastUser.
