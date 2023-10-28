from django.urls import path
from .views import iniciar_sesion

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='login'),
]