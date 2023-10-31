from django.shortcuts import render
from crudEgresados.models import Egresado
from django.db.models import Count, Window, F
from django.db.models.functions import Rank
from django.http import JsonResponse


'''from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view'''

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    if request.method == 'GET':
        egresados = Egresado.objects.all()[:1000]
        return render(request, 'dashboard.html', {'egresados': egresados})

def manual(request):
    return render(request, 'inicio.html')

def grafica_dinamica1(request):
    egresados = Egresado.objects.filter(ciudad__isnull=False).values('ciudad').annotate(total_egresados=Count('id'))
    egresados = sorted(egresados, key=lambda x: x['total_egresados'], reverse=True)[:10]
    data = list(egresados)

    return JsonResponse(data, safe=False)

def grafica_dinamica2(request):
    egresados = Egresado.objects.values('nivel_educativo').annotate(total_egresados=Count('id'))
    egresados = sorted(egresados, key=lambda x: x['total_egresados'], reverse=True)[:10]
    data = list(egresados)

    return JsonResponse(data, safe=False)