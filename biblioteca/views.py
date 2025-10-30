from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor, Genero
from .forms import LivroForm
from django.contrib import messages
from .forms import  RegisterForm# ✅ nome correto do formulário de cadastro

def register(request):  # ✅ você pode manter o nome register
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # cria o usuário no banco
            return redirect('login')  # ✅ corrigido (antes estava 'homw')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def home(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('lista_livros')
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
            form.save(request=request)
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
