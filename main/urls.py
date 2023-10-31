from django.urls import path
from .views import home, manual, dashboard, grafica_dinamica1, grafica_dinamica2

urlpatterns = [
    path('', home, name='inicio'),
    path('manual/', manual, name='manual'),
    path('dashboard/', dashboard, name='Dashboard'),


    path('grafica_dinamica1/', grafica_dinamica1, name='grafica_dinamica1'),
    path('grafica_dinamica2/', grafica_dinamica2, name='grafica_dinamica2')
]