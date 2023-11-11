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
    path('sectores', sectores, name='sectores'),
    path('sectores/eliminar/<int:sector_id>', eliminar_sector, name='eliminar_sector'),
    path('sectores/editar/<int:sector_id>', editar_sector, name='editar_sector'),
    path('sectores_egresados', sectores_egresados, name='sectores_egresados'),
    path('sectores_egresados/eliminar/<int:sector_egresado_id>', eliminar_sector_egresado, name='eliminar_sector_egresado'),
    path('sectores_egresados/editar/<int:sector_egresado_id>', editar_sector_egresado, name='editar_sector_egresado'),
]
