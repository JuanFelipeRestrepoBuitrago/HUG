from django.urls import path
from .views import *

urlpatterns = [
    path('egresados', EgresadosView.as_view(), name='egresados'),
    path('egresados/eliminar/<int:egresado_id>', EgresadosEliminarView.as_view(), name='eliminar_egresado'),
    path('egresados/editar/<int:egresado_id>', EgresadosEditarView.as_view(), name='editar_egresado'),
    path('estudios', EstudiosView.as_view(), name='estudios'),
    path('estudios/eliminar/<int:estudio_id>', EstudiosEliminarView.as_view(), name='eliminar_estudio'),
    path('estudios/editar/<int:estudio_id>', EstudiosEditarView.as_view(), name='editar_estudio'),
    path('experiencias', ExperienciasView.as_view(), name='experiencias'),
    path('experiencias/eliminar/<int:experiencia_id>', ExperienciasEliminarView.as_view(), name='eliminar_experiencia'),
    path('experiencias/editar/<int:experiencia_id>', ExperienciasEditarView.as_view(), name='editar_experiencia'),
    path('sectores', SectoresView.as_view(), name='sectores'),
    path('sectores/eliminar/<int:sector_id>', SectoresEliminarView.as_view(), name='eliminar_sector'),
    path('sectores/editar/<int:sector_id>', SectoresEditarView.as_view(), name='editar_sector'),
    path('sectores_egresados', SectoresEgresadosView.as_view(), name='sectores_egresados'),
    path('sectores_egresados/eliminar/<int:sector_egresado_id>', SectoresEgresadosEliminarView.as_view(), name='eliminar_sector_egresado'),
    path('sectores_egresados/editar/<int:sector_egresado_id>', SectoresEgresadosEditarView.as_view(), name='editar_sector_egresado'),
]
