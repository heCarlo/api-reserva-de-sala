# core/urls.py
from django.urls import path, include  # Importe include corretamente

urlpatterns = [
    # Outras URLs do projeto
    path('api/', include('app.urls')),  # Inclui as URLs do app
]
