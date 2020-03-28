from django import forms
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Event
from .forms import UserUpdateForm, EventCreateForm

# Create your views here.
def listfunc(request):
    object_list = Event.objects.all()
    if request.user.is_authenticated:
        print('yes')
        user = User.objects.get(pk=request.user.pk)
        return render(request, 'list.html',{'object_list':object_list,'user':user})
    else:
        print('no')
        return render(request, 'list.html',{'object_list':object_list})


def createeventfunc(request):
    if request.method == 'POST':
        form =EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,'createevent.html',{'form':form})
        
    else:
        default_data = {'author':User.objects.get(pk=request.user.pk)}
        form =EventCreateForm(default_data)
        return render(request,'createevent.html',{'form':form})



def signupfunc(request):
    if request.method ==  'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html',{'error':'This username is already exist'})
        except:
            user = User.objects.create_user(username,'',password)
            object_list = Event.objects.all()
            # user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('list')
    return render(request, 'signup.html')

def loginfunc(request, event_pk=None):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if event_pk:
                event = Event.objects.filter(pk=event_pk)
                return render(request,'detail.html',{'event':event})
            else:
                return redirect('list')
        else:
            print('why')
            if event_pk:
                event = Event.objects.filter(pk=event_pk)
                return render(request,'login.html',{'event':event})
            else:
                return redirect('login')

    return render(request, 'login.html')

def logoutfunc(request):
    logout(request)
    return redirect('login')

def usermypagefunc(request, current_status):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        event_list = Event.objects.filter(author=request.user.pk)
        return render(request, 'mypage/mypage.html',{'user':user,'current_status':current_status,'event_list':event_list})
    else:
        return redirect('login')

def detailfunc(request, event_pk):
    event = Event.objects.filter(pk=event_pk)
    if request.user.is_authenticated:
        return render(request, 'detail.html',{'event':event})
    else:
        return redirect('login',event_pk=event_pk)
    
