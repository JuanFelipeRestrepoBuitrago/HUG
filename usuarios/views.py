from django.shortcuts import render, redirect


def login2(request):
    if request.user.is_authenticated:
        redirect('inicio')
    return render(request, 'login.html')


def login(request):
    if request.user.is_authenticated:
        redirect('inicio')
    return render(request, 'signin.html')
