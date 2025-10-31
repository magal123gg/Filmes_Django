from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor, Genero
from .forms import LivroForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    print('REGISTRAR')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # cria o usuário no banco
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect('login')  # redireciona corretamente
    else:
        form = RegisterForm()

    return render(request, 'registrar.html', {'form': form})


def home(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()  # removido o request=request
            messages.success(request, "Livro adicionado com sucesso!")
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
            form.save()  # removido o request=request
            messages.success(request, "Livro adicionado com sucesso!")
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
            messages.success(request, "Livro editado com sucesso!")
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'editar_livro.html', {'form': form})


def deletar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    if request.method == 'POST':
        livro.delete()
        messages.success(request, "Livro deletado com sucesso!")
        return redirect('lista_livros')
    return render(request, 'deletar_livro.html', {'livro': livro})

@login_required
def perfil(request):
    return render(request, 'perfil.html')
