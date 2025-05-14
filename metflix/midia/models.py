from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(unique=False, blank=True, null=True)

    def __str__(self):
        return self.username

    @property
    def biblioteca(self):
        jogos = [uj.jogo for uj in self.jogos_adquiridos.all()]
        filmes_series = [ufs.filme_serie for ufs in self.filmes_series_assistidos.all()]
        return {
            'jogos': jogos,
            'filmes_series': filmes_series
        }

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    data_lancamento = models.IntegerField()
    preco = models.FloatField()

    def __str__(self):
        return self.nome

class FilmeSerie(models.Model):
    CATEGORIA_CHOICES = [
        ('Filme', 'Filme'),
        ('Serie', 'Série'),
    ]

    nome = models.CharField(max_length=100)
    data_lancamento = models.IntegerField()
    genero = models.CharField(max_length=50)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.categoria})"
    

class UsuarioJogo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='jogos_adquiridos')
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.jogo.nome}"

class UsuarioFilmeSerie(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='filmes_series_assistidos')
    filme_serie = models.ForeignKey(FilmeSerie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.filme_serie.nome}"