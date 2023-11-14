from django.shortcuts import render
from crudEgresados.models import Egresado, SectoresEgresados, Sector
from django.db.models import Count, Window, F, Avg, Count
from django.http import JsonResponse
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    """
    Esta funcion realiza una consulta que obtiene los datos de los primeros 1000 egresados y los envia a la pagina dashboard.html si
    el metodo de la peticion es GET
    @param request:
    @return render: retorna la pagina dashboard.html con los datos de los primeros 1000 egresados
    """
    if request.method == 'GET':
        egresados = Egresado.objects.all()[:1000]
        return render(request, 'dashboard.html', {'egresados': egresados})

def manual(request):
    return render(request, 'inicio.html')

def grafica_dinamica1(request):
    """
    Esta funcion realiza una consulta que obtiene los datos de las 10 ciudades con mayor numero de egresados
    @param request:
    @return data: retorna un json con los datos de ciudad y total_egresados
    """
    egresados = Egresado.objects.filter(ciudad__isnull=False).values('ciudad').annotate(total_egresados=Count('id'))
    egresados = sorted(egresados, key=lambda x: x['total_egresados'], reverse=True)[:10]
    data = list(egresados)

    return JsonResponse(data, safe=False)

def grafica_dinamica2(request):
    """
    Esta funcion realiza una consulta del tototal de egresados por nivel educativo
    @param request:
    @return data: retorna un json con los datos de nivel_educativo y total_egresados
    """
    egresados = Egresado.objects.values('nivel_educativo').annotate(total_egresados=Count('id'))
    egresados = sorted(egresados, key=lambda x: x['total_egresados'], reverse=True)[:10]
    data = list(egresados)

    return JsonResponse(data, safe=False)

def grafica_dinamica3(request):
    """
    Esta funcion realiza una consulta que obtiene los datos de nivel_educativo y salario_promedio correspondientes a cada nivel educativo
    @param request:
    @return: data: retorna un json con los datos de nivel_educativo y salario_promedio
    """
    egresados = Egresado.objects.values('nivel_educativo').annotate(salario_promedio=Avg('salario'))
    data = list(egresados)
    for diccionario in data:
        diccionario['salario_promedio'] = int(diccionario['salario_promedio'])

    return JsonResponse(data, safe=False)

def grafica_dinamica4(request):
    """
    Esta funcion realiza una consulta que la experiencia promedio en meses de los egresados dependiendo su nivel educativo
    @param request:
    @return: data: retorna un json con los datos de nivel_educativo y numero_egresados
    """
    egresados = Egresado.objects.values('nivel_educativo').annotate(experiencia_promedio=Avg('experiencia_meses'))
    data = list(egresados)

    for diccionario in data:
        diccionario['experiencia_promedio'] = int(diccionario['experiencia_promedio'])
        if diccionario['nivel_educativo'] == "Bachillerato (grados 6°, 7° u 8°)":
            diccionario['nivel_educativo'] = "Bachillerato (6°, 7° u 8°)"
        if diccionario['nivel_educativo'] == "Bachillerato (grados 9°, 10° y 11°)":
            diccionario['nivel_educativo'] = "Bachillerato (9°, 10° y 11°)"
        if diccionario['nivel_educativo'] == "Especialización/ Maestría":
            diccionario['nivel_educativo'] = "Postgrado"

    return JsonResponse(data, safe=False)

def grafica_dinamica5(request):
    """
    Esta funcion realiza una consulta que obtiene los datos de experiencia_meses y salario de los primeros 2000 egresados
    @param request:
    @return: data: retorna un json con los datos de experiencia_meses y salario de los primeros 2000 egresados
    """
    data = list([])
    egresados = Egresado.objects.values('experiencia_meses', 'salario')[:2000]
    for egresado in egresados:
        data.append(list([int(egresado['experiencia_meses']), int(egresado['salario'])]))

    return JsonResponse(data, safe=False)

def grafica_dinamica6(request):
    """
    Esta función realiza una consulta que obtiene los 15 sectores laborales a los que más egresados están asociados
    @param request:
    @return data: retorna un json con los datos
    """
    egresados = Sector.objects.annotate(cantidad=Count('sectoresegresados__egresado')).order_by('-cantidad')
    data = list([])
    for objeto in egresados:
        data.append({"category":objeto.nombre, "value":objeto.cantidad})

    return  JsonResponse(data, safe=False)
