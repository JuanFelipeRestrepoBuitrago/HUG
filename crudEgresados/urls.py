from django.urls import path
from .views import egresados

urlpatterns = [
    path('', egresados, name='egresados'),
]