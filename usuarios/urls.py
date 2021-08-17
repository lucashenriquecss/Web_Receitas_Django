from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('criar/receita', views.criar_receita, name='criar_receita'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('editar/<int:receita_id>', views.editar_receita, name='editar_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita'),

    
]
