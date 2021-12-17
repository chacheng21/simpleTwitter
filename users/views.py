from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout


# Create your views here.
from .models import *
from .forms import CreateUserForm

app_name = 'users'


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
        else: 
            form = CreateUserForm()
            context = {'form': form, 'error': True}
            return render(request, "register.html", context)


    context = {'form': form, 'error': False}
    return render(request, "register.html", context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('hello')
            login(request, user)
            return redirect('tweets:home_page')
        else:
            context = {'error': True}
            return render(request, 'login.html', context)
    
    context = {'error': False}
    return render(request, 'login.html', context)

def logout(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('/login')

def splashPage(request):
    return render(request, 'splash.html')
