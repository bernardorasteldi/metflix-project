from django.contrib import admin
from .models import Usuario, Jogo, FilmeSerie, UsuarioJogo, UsuarioFilmeSerie

admin.site.register(Usuario)
admin.site.register(Jogo)
admin.site.register(FilmeSerie)
admin.site.register(UsuarioJogo)
admin.site.register(UsuarioFilmeSerie)
