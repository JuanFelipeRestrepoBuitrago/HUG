from django.urls import path
from .views import *

urlpatterns = [
    path('iniciar_sesion/', IniciarSesionView.as_view(), name='login'),
    path('cerrar_sesion/', CerrarSesionView.as_view(), name='logout'),
    path('registrarse/', RegistrarseView.as_view(), name='signup'),
]
