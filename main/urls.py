from django.urls import path
from .views import home, manual

urlpatterns = [
    path('', home, name='inicio'),
    path('manual/', manual, name='manual'),
]