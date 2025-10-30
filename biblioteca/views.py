# Sua_Pasta_do_Projeto/biblioteca/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor, Genero
from .forms import LivroForm # Criaremos este formulário mais tarde
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save(request=request)  # Passa o request para o método save
            return redirect('lista_livros') # Redireciona para a lista após salvar
    else:
        form = LivroForm()
    return render(request, 'home.html', {'form': form})

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})


def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save(request=request)  # Passa o request para o método save
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'adicionar_livro.html', {'form': form})


def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'editar_livro.html', {'form': form})

def deletar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'deletar_livro.html', {'livro': livro})
