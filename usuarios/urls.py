from django.urls import path
from .views import iniciar_sesion, cerrar_sesion, registrarse

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='login'),
    path('cerrar_sesion/', cerrar_sesion, name='logout'),
    path('registrarse/', registrarse, name='signup'),
]
