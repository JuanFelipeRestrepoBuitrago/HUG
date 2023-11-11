from django.urls import path
from .views import *

urlpatterns = [
    path('egresados', egresados, name='egresados'),
    path('egresados/eliminar/<int:egresado_id>', eliminar_egresado, name='eliminar_egresado'),
    path('egresados/editar/<int:egresado_id>', editar_egresado, name='editar_egresado'),
    path('estudios', estudios, name='estudios'),
]