from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from abc import ABC, abstractmethod
from django.views import View


class UsuariosView(View):
    template_name = ''

    def get(self, request):
        """
        Esta función permite renderizar la página de la vista.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        if request.user.is_authenticated:
            return redirect('inicio')
        return render(request, self.template_name)

    @abstractmethod
    def post(self, request):
        """
        Esta función permite procesar la información enviada por el usuario a través de un formulario.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        pass


class IniciarSesionView(UsuariosView):
    template_name = 'signin.html'

    def post(self, request):
        """
        Esta función permite iniciar sesión en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        username = request.POST['username']
        password = request.POST['password']
        try:
            usuario = CustomUser.iniciar_sesion(request, username, password)
            # Si el usuario es un administrador, se redirige a la página de administración, de lo contrario,
            # se redirige a la página de inicio.
            if usuario.user_type == 'admin':
                return redirect('egresados')
            else:
                return redirect('inicio')
        except CustomUser.DoesNotExist:
            messages.error(request, 'El usuario no existe')
            return redirect('login')
        except IntegrityError as error:
            messages.error(request, error)
            return redirect('login')


@method_decorator(login_required, name='dispatch')
class CerrarSesionView(View):
    def get(self, request):
        """
        Esta función permite cerrar sesión en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        CustomUser.cerrar_sesion(request)
        return redirect('inicio')

    def post(self, request):
        """
        Esta función permite cerrar sesión en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
        CustomUser.cerrar_sesion(request)
        return redirect('inicio')


class RegistrarseView(UsuariosView):
    template_name = 'signup.html'

    def post(self, request):
        """
        Esta función permite registrar un usuario en el sistema.
        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual.
        @return: HttpResponse, objeto que contiene la respuesta HTTP que se enviará al navegador web que realizó la
        """
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
