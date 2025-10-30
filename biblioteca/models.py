from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=100)
    generos = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # gera o slug com base no título
        if not self.slug:
            self.slug = slugify(self.titulo)

        # verifica se já existe livro com o mesmo slug (ou título)
        if Livro.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError("❌ Já existe um livro com este título!")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
