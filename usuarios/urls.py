from django.urls import path
from .views import iniciar_sesion, login2

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='login'),
    path('login/', login2, name='signin'),
]