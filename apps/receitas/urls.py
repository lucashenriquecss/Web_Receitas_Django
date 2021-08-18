from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
    path('criar/receita', criar_receita, name='criar_receita'),
    path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('editar/<int:receita_id>', editar_receita, name='editar_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita'),

]
