from django.shortcuts import render, redirect
from .models import CustomUser
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login2(request):
    if request.user.is_authenticated:
        redirect('inicio')
    return render(request, 'login.html')


def signin(request):
    if request.user.is_authenticated:
        redirect('inicio')
    elif request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            username = CustomUser.objects.get(Q(username=username) | Q(email=username)).username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
                return redirect('login')
        except CustomUser.DoesNotExist:
            messages.error(request, 'El usuario no existe')
            return redirect('login')
