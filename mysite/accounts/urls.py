# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    # Puedes añadir más URLs de cuentas aquí si las necesitas
]
