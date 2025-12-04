from django.shortcuts import render, redirect
from . models import mens, womens,accessoriess
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
def home(request):
    womens_items = womens.objects.all()
    accessoriess_items = accessoriess.objects.all()
    mens_items = mens.objects.all()
    context = {
         'mens_items': mens_items,
         'womens_items': womens_items,
         'accessoriess_items': accessoriess_items
    }

    return render(request, 'home.html', context)
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user= User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('home')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
def logout(request):
    auth_logout(request)
    return redirect('home')