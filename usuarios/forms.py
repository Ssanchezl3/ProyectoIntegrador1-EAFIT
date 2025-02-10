from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comprador

class RegistroUsuarioForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=False)
    direccion = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Comprador
        fields = ["username", "email", "telefono", "direccion", "password1", "password2"]
