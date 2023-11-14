from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.db import IntegrityError


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    institution = models.CharField(max_length=500, null=True, blank=True)
    user_type = models.CharField(max_length=5, default='admin', choices=(('user', 'user'), ('admin', 'admin')))

    def __str__(self):
        """
        Esta función permite obtener el nombre de usuario cuando se imprime un objeto de la clase CustomUser
        @return: retorna el nombre de usuario
        """
        return self.username

    @staticmethod
    def iniciar_sesion(request, username, password):
        """
        Esta función permite iniciar sesion en el sistema

        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual
        @param username: nombre de usuario o correo electrónico
        @param password: contraseña
        @return:
        """
        # Recupera el nombre de usuario si se ingresó el correo electrónico
        username = CustomUser.objects.get(Q(username=username) | Q(email=username)).username
        # Se autentica el usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Se inicia sesion
            login(request, user)
            return user
        else:
            raise IntegrityError('Usuario o contraseña incorrectos')

    @staticmethod
    def cerrar_sesion(request):
        """
        Esta función permite cerrar sesion en el sistema

        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual
        """

        # Se cierra sesion
        logout(request)

    @staticmethod
    def registrarse(request, username, email, first_name, last_name, institution, password, confirm_password):
        """
        Esta función permite registrar un usuario en el sistema

        @param request: HttpRequest, objeto que contiene la información sobre la solicitud web actual
        @param username: nombre de usuario
        @param email: correo electrónico
        @param first_name: Nombre del usuario
        @param last_name: Apellido del usuario
        @param institution: Institución a la que pertenece el usuario
        @param password: Contraseña
        @param confirm_password: Confirmación de la contraseña
        """
        if password != confirm_password:
            raise IntegrityError('Las contraseñas no coinciden')
        user = CustomUser(username=username, email=email, first_name=first_name, last_name=last_name,
                          institution=institution, user_type='user', password=password)

        user.save()
        login(request, user)
        return user
