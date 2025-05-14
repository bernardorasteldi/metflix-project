from django import forms
from .models import Jogo, FilmeSerie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome', 'data_lancamento', 'preco']

class FilmeSerieForm(forms.ModelForm):
    class Meta:
        model = FilmeSerie
        fields = ['nome', 'data_lancamento', 'genero', 'categoria']

Usuario = get_user_model()

class UsuarioCreationForm(UserCreationForm): 
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2']
