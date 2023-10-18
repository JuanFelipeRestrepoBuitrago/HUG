from django.urls import path
from .views import signin, login2

urlpatterns = [
    path('iniciar_sesion/', signin, name='login'),
    path('login/', login2, name='signin'),
]