from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def iniciar_sesion(request):
    """
    Esta función permite iniciar sesión en el sistema.

    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se
    enviará al navegador web que realizó la solicitud.
    """

    # Si el usuario ya está autenticado, se redirige a la página de inicio.
    if request.user.is_authenticated:
        return redirect('inicio')
    # Si el método de la petición es GET, se muestra el formulario de inicio de sesión.
    elif request.method == 'GET':
        return render(request, 'signin.html')
    # Si el método de la petición es POST, se intenta iniciar sesión.
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            usuario = CustomUser.iniciar_sesion(request, username, password)
            # Si el usuario es un administrador, se redirige a la página de administración, de lo contrario,
            # se redirige a la página de inicio.
            if usuario.user_type == 'admin':
                return redirect('inicio')  # TODO: Cambiar a admin
            else:
                return redirect('inicio')
        except CustomUser.DoesNotExist:
            messages.error(request, 'El usuario no existe')
            return redirect('login')
        except IntegrityError as error:
            messages.error(request, error)
            return redirect('login')


@login_required
def cerrar_sesion(request):
    """
    Esta función permite cerrar sesión en el sistema.

    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se
    enviará al navegador web que realizó la solicitud.
    """

    CustomUser.cerrar_sesion(request)
    return redirect('inicio')


def registrarse(request):
    """
    Esta función permite registrar un usuario en el sistema.

    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se
    enviará al navegador web que realizó la solicitud.
    """

    # Si el usuario ya está autenticado, se redirige a la página de inicio.
    if request.user.is_authenticated:
        return redirect('inicio')
    # Si el método de la petición es GET, se muestra el formulario de registro.
    elif request.method == 'GET':
        return render(request, 'signup.html')
    # Si el método de la petición es POST, se intenta registrar el usuario.
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        institution = request.POST['institution']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        try:
            CustomUser.registrarse(request, username, email, first_name, last_name, institution, password,
                                   confirm_password)
            return redirect('inicio')
        except IntegrityError as error:
            messages.error(request, error)
            return redirect('signup')