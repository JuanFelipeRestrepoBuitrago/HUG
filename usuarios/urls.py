from django.urls import path
from .views import login

urlpatterns = [
    path('iniciar_sesion/', login, name='login'),
]