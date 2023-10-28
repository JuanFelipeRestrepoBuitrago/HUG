from django.shortcuts import render, redirect
from .models import CustomUser
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def iniciar_sesion(request):
    """
    Esta función permite iniciar sesión en el sistema. Si el usuario ya está autenticado, se redirige a la página de inicio.
    Si el usuario no está autenticado, se muestra el formulario de inicio de sesión. Si el usuario no existe, se muestra un
    mensaje de error. Si el usuario existe, pero la contraseña es incorrecta, se muestra un mensaje de error.

    @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
    @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la solicitud.
    """
    if request.user.is_authenticated:
        return redirect('inicio')
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
