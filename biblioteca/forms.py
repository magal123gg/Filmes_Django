from django import forms
from .models import Livro, Autor, Genero
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'generos']

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        slug = slugify(titulo)

        # Verifica se já existe livro com mesmo slug (ou título)
        if Livro.objects.filter(slug=slug).exists():
            raise forms.ValidationError("❌ Já existe um livro com este título!")

        return titulo

