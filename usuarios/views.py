from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirigir a login después del registro
    else:
        form = UserCreationForm()

    return render(request, "usuarios/registro.html", {"form": form})

def foro(request):
    return render(request, "foro/foro.html")

