from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Egresado
from usuarios.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def egresados(request):
    """
    Esta función permite listar los egresados en el sistema. También permite crear, actualizar y eliminar egresados con
    formularios que redirigen a la página con la acción correspondiente.
    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
    """
    if request.user.user_type == 'user':
        return redirect('inicio')
    if request.method == 'GET':
        egresados_objects = Egresado.objects.all()
        return render(request, 'egresados.html', {
            'egresados': egresados_objects
        })
    elif request.method == 'POST':
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        if fecha_nacimiento == '' or fecha_nacimiento == ' ':
            fecha_nacimiento = None
        nivel_educativo = request.POST.get('nivel_educativo')
        if nivel_educativo == '' or nivel_educativo == ' ':
            nivel_educativo = None
        salario = request.POST.get('salario')
        if salario == '' or salario == ' ':
            salario = None
        experiencia_meses = request.POST.get('experiencia_meses')
        if experiencia_meses == '' or experiencia_meses == ' ':
            experiencia_meses = None
        ciudad = request.POST.get('ciudad')
        if ciudad == '' or ciudad == ' ':
            ciudad = None

        try:
            Egresado.crear_egresado(fecha_nacimiento, nivel_educativo, salario, experiencia_meses, ciudad)
            messages.success(request, 'Egresado creado correctamente')
        except IntegrityError as e:
            messages.error(request, e)
        finally:
            return redirect('egresados')

