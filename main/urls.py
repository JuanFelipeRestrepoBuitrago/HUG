from django.urls import path
from .views import home, manual, dashboard

urlpatterns = [
    path('', home, name='inicio'),
    path('manual/', manual, name='manual'),
    path('dashboard/', dashboard, name='Dashboard'),
]