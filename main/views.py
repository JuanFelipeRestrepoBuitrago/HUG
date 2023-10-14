from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def manual(request):
    return render(request, 'inicio.html')