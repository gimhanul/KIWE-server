from django.contrib.auth import authenticate, login, logout
from .models import User, FriendRequest, Profile, Notification
from django.shortcuts import redirect, render
from .forms import UserCreationForm, AuthenticationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
import json


def index(request):
    return render(request, 'index.html')



#join
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



#login
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



#main
def kiwe(request):
    if request.method == 'POST':
        return redirect('../q/1')
    return render(request, 'kiwe.html')



#setting
def setting(request):
    if request.method == 'POST':
        setting = request.POST.get('setting')
        if setting == 'logout':
            logout(request)
            return redirect('/')
        elif setting == 'profile':
            print(".")
    return render(request, 'setting.html')



#friends
def friends(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        result = User.objects.filter(email=data).values('profile')[0]['profile']
        result = Profile.objects.get(id = result)
        result = result.__dict__
        del result['_state']
        print(result)
        return JsonResponse(result, safe=False)


    temp = User.objects.get(id=request.user.id).friends.values('profile')
    temp = [i['profile'] for i in temp]
    friends = []
    for i in temp:
        temp1 = Profile.objects.filter(id=i).values('name', 'description', 'image', 'id')[0]
        friends.append(temp1)

    
    context = {
        'friends': friends
    }
    return render(request, 'friends.html', context)


def send_friend_request(i, user_id):
    from_user = i
    to_user = User.objects.get(id = user_id)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created:
        notiCreate(to_user, from_user, 'request', created.id)
        return
    else:
        return
        

def accept_friend_request(user, requestID):
    fr = FriendRequest.objects.get(id=requestID)
    if fr.to_user == user:
        fr.to_user.friends.add(fr.from_user)
        fr.from_user.friends.add(fr.to_user)
        notiCreate(fr.from_user, fr.to_user, 'accept', '\0')
        fr.delete()
        return
    else:
        return


def delete_friend_request(user, requestID):
    fr = FriendRequest.objects.get(id=requestID)
    if fr.to_user == user:
        fr.delete()
        return
    else:
        return



#profile
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
        form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {

        'form': form
    }

    return render(request, 'profileEdit.html', context)



#notification
def notification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['at']=='accept':
            accept_friend_request(request.user, data['requestID'])
        elif data['at'] == 'no':
            delete_friend_request(request.user, data('requestID'))

    notification = Notification.objects.filter(to_user = request.user)
    context = {
        'notification': notification
    }
    return render(request, 'notification.html', context)

def notiCreate(to_user, from_user, notitype, requestID):
    noti = Notification.objects.create(
        to_user = to_user,
        from_user = from_user,
        notitype = notitype,
        requestID = requestID
    )
    noti.save()