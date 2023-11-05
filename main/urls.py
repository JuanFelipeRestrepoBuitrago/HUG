from django.urls import path
from .views import home, manual, dashboard, grafica_dinamica1, grafica_dinamica2, grafica_dinamica3, grafica_dinamica4, grafica_dinamica5

urlpatterns = [
    path('', home, name='inicio'),
    path('manual/', manual, name='manual'),
    path('dashboard/', dashboard, name='Dashboard'),


    path('grafica_dinamica1/', grafica_dinamica1, name='grafica_dinamica1'),
    path('grafica_dinamica2/', grafica_dinamica2, name='grafica_dinamica2'),
    path('grafica_dinamica3/', grafica_dinamica3, name='grafica_dinamica3'),
    path('grafica_dinamica4/', grafica_dinamica4, name='grafica_dinamica4'),
    path('grafica_dinamica5/', grafica_dinamica5, name='grafica_dinamica5')
]