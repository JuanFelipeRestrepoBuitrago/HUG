from django.urls import path
from .views import egresados, eliminar_egresado

urlpatterns = [
    path('', egresados, name='egresados'),
    path('eliminar_egresado/<int:egresado_id>', eliminar_egresado, name='eliminar_egresado')
]