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

