from django.urls import path
from .views import *

urlpatterns = [
    path('egresados', egresados, name='egresados'),
    path('egresados/eliminar/<int:egresado_id>', eliminar_egresado, name='eliminar_egresado'),
    path('egresados/editar/<int:egresado_id>', editar_egresado, name='editar_egresado'),
    path('estudios', estudios, name='estudios'),
    path('estudios/eliminar/<int:estudio_id>', eliminar_estudio, name='eliminar_estudio'),
    path('estudios/editar/<int:estudio_id>', editar_estudio, name='editar_estudio'),
    path('experiencias', experiencias, name='experiencias'),
    path('experiencias/eliminar/<int:experiencia_id>', eliminar_experiencia, name='eliminar_experiencia'),
    path('experiencias/editar/<int:experiencia_id>', editar_experiencia, name='editar_experiencia'),
]