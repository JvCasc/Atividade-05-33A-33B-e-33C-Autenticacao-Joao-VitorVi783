from django.db import models

class Filmes(models.Model):
  title = models.CharField(max_length=50)
  director = models.CharField(max_length=70)
  genre = models.CharField(max_length=20)
  release_date = models.DateField()

class Livros(models.Model):
  title = models.CharField(max_length=50)
  director = models.CharField(max_length=70)
  genre = models.CharField(max_length=20)
  nota = models.CharField(max_length=20)