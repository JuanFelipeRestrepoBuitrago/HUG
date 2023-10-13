from django.shortcuts import render, redirect


def login(request):
    if request.user.is_authenticated:
        redirect('inicio')
    return render(request, 'login.html')
