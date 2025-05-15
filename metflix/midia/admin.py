from django.contrib import admin
from .models import Usuario, Jogo, FilmeSerie, UsuarioJogo, UsuarioFilmeSerie

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ['username']

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'data_lancamento', 'preco']

@admin.register(FilmeSerie)
class FilmeSerieAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'categoria', 'data_lancamento', 'genero']
    list_filter = ['categoria']

@admin.register(UsuarioJogo)
class UsuarioJogoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'jogo']

@admin.register(UsuarioFilmeSerie)
class UsuarioFilmeSerieAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'filme_serie']