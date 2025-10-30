from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),

    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),

    path('editar/<int:livro_id>/', views.editar_livro, name='editar_livro'),

    path('deletar/<int:livro_id>/', views.deletar_livro, name='deletar_livro'),
]
