from django.urls import path
from .views import login, login2

urlpatterns = [
    path('iniciar_sesion/', login, name='login'),
    path('login/', login2, name='signin'),
]