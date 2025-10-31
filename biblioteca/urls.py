from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),

    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('editar/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('deletar/<int:livro_id>/', views.deletar_livro, name='deletar_livro'),

    
    path('registrar/', views.register, name='registrar'),

    path('login/', auth_views.LoginView.as_view(template_name='home.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('perfil/', views.perfil, name='perfil'),
]
