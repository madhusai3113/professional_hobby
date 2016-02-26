from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils import timezone
from .models import User

# Create your views here.
def home(request):
    if('username' not in request.session):
        return HttpResponseRedirect(reverse('baseapp:login'))
    return render(request,'baseapp/index.html',{'user' : request.session['username'] })

def login(request):
    if 'username' in request.session:
        return HttpResponseRedirect(reverse('baseapp:home'))
    return render(request,'baseapp/login.html',{})

def doLogin(request):
    if ('username' in request.POST and 'password' in request.POST):
        u = User.objects.get(username=request.POST['username'])
        if u.password == request.POST['password']:
            request.session['username'] = request.POST['username']
            return HttpResponseRedirect(reverse('baseapp:home'))
        else:
            messages.success(request,"Invalid username/password combination.")
            return HttpResponseRedirect(reverse('baseapp:login'))
    else:
        return HttpResponseRedirect(reverse('baseapp:home'))

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('baseapp:login'))

def register(request):
    if('username' in request.POST):
        u = User(username = request.POST['username'], email = request.POST['email'], password = request.POST['password'])
        u.save()
        request.session['username'] = request.POST['username']
        return HttpResponseRedirect(reverse('baseapp:index'))
    else:
        messages.success(request,"Unable to receive request.")
        return HttpResponseRedirect(reverse('baseapp:sign_up'))

def sign_up(request):
    return render(request,'baseapp/sign_up.html',{})

def show_users(request):
    user = request.session['username']
    a = User.objects.exclude(username = request.session['username'])
    return render(request,'baseapp/users.html',{ 'users' : a, 'user' : user })

def connect(request,username):
    return render(request, 'baseapp/username',{  })