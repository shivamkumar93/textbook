from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout



def authlogin(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    form = LoginForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            login_user = authenticate(username=username, password=password)
            if login_user is not None:
                login(request, login_user)
                return redirect('homepage')

    return render(request, "auth/login.html", {'form':form})

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            password = form.cleaned_data.get('password')

            data = form.save(commit=False)
            data.set_password(password)
            data.save()
            return redirect('authlogin')
    return render(request, 'auth/register.html', {'form':form})

def authlogout(request):
    logout(request)
    return redirect('authlogin')
    