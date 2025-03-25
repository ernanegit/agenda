# Atualize o arquivo contatos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    
    # Adicione estas linhas ao urlpatterns
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    path('criar/', views.criar_contato, name='criar_contato'),
    path('<int:contato_id>/editar/', views.editar_contato, name='editar_contato'),
    path('<int:contato_id>/deletar/', views.deletar_contato, name='deletar_contato'),
]