from django.urls import path
from .views.salaView import *

urlpatterns = [
    path('api/salas/', SalaList.as_view()),
    path('api/salas/<int:pk>/', SalaDetail.as_view()),
    path('salas/listar/', listar_salas),
    path('salas/criar/', criar_sala),
    path('salas/<int:sala_id>/atualizar/', atualizar_sala),
    path('salas/<int:sala_id>/excluir/', excluir_sala),
]
