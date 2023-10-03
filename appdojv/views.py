from django.shortcuts import render, redirect
from .models import Filmes, Livros
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  filmes = Filmes.objects.all()
  livros = Livros.objects.all()
  
  return render(request, "home.html", context={ 
    "filmes": filmes,
    "livros": livros
  })

@login_required
def create_filme(request):
  if request.method == "POST":
    Filmes.objects.create(
      title = request.POST["title"],
      director = request.POST["director"],
      genre = request.POST["genre"],
      release_date = request.POST["release_date"]
    )

    return redirect("home")
  return render(request, "forms.html", context={"action": "Adicionar"})

@login_required
def update_filme(request, id):
  filme = Filmes.objects.get(id = id)
  if request.method == "POST":
    filme.title = request.POST["title"]
    filme.director = request.POST["director"]
    filme.genre = request.POST["genre"]
    filme.release_date = request.POST["release_date"]
    filme.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","filme": filme})

@login_required
def delete_filme(request, id):
  filme = Filmes.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      filme.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"filme": filme})

@login_required
def create_livro(request):
  if request.method == "POST":
    Livros.objects.create(
      title = request.POST["title"],
      director = request.POST["director"],
      genre = request.POST["genre"],
    )

    return redirect("home")
  return render(request, "forms2.html", context={"action": "Adicionar"})

@login_required
def update_livro(request, id):
  livro = Livros.objects.get(id = id)
  if request.method == "POST":
    livro.title = request.POST["title"]
    livro.director = request.POST["director"]
    livro.genre = request.POST["genre"]
    livro.nota = request.POST["nota"]
    livro.save()

    return redirect("home")
  return render(request, "forms2.html", context={"action": "Atualizar","livro": livro})

@login_required
def delete_livro(request, id):
  livro = Livros.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      livro.delete()

    return redirect("home")
  return render(request, "are_you_sure2.html", context={"livro": livro})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")