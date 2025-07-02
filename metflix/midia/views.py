from django.contrib.auth import login as auth_login, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


from .forms import UsuarioCreationForm
from .models import FilmeSerie, Jogo, UsuarioFilmeSerie, UsuarioJogo


@login_required(login_url='login')
def adicionar_jogo_biblioteca(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)
    _, created = UsuarioJogo.objects.get_or_create(usuario=request.user, jogo=jogo)

    if created:
        messages.success(request, f'"{jogo.nome}" adicionado à sua biblioteca!')
    else:
        messages.info(request, f'"{jogo.nome}" já está na sua biblioteca.')

    return redirect('lista_jogos')

@login_required(login_url='login')
def adicionar_filme_serie_biblioteca(request, filme_id):
    filme_serie = FilmeSerie.objects.get(id=filme_id)
    _, created = UsuarioFilmeSerie.objects.get_or_create(usuario=request.user, filme_serie=filme_serie)

    if created:
        messages.success(request, f'"{filme_serie.nome}" adicionado à sua biblioteca!')
    else:
        messages.info(request, f'"{filme_serie.nome}" já está na sua biblioteca.')

    return redirect('lista_filmes_series')

@login_required(login_url='login')
def remover_jogo_biblioteca(request, jogo_id):
    jogo = get_object_or_404(Jogo, id=jogo_id)
    
    deletado, _ = UsuarioJogo.objects.filter(
        usuario=request.user,
        jogo=jogo
    ).delete()
    
    if deletado:
        messages.success(request, f'"{jogo.nome}" removido da sua biblioteca.')
    else:
        messages.info(request, f'"{jogo.nome}" não estava na sua biblioteca.')

    return redirect('biblioteca')


@login_required(login_url='login')
def remover_filme_serie_biblioteca(request, filme_id):
    filme_serie = get_object_or_404(FilmeSerie, id=filme_id)
    
    deletado, _ = UsuarioFilmeSerie.objects.filter(
        usuario=request.user,
        filme_serie=filme_serie
    ).delete()
    
    if deletado:
        messages.success(request, f'"{filme_serie.nome}" removido da sua biblioteca.')
    else:
        messages.info(request, f'"{filme_serie.nome}" não estava na sua biblioteca.')

    return redirect('biblioteca')

@login_required(login_url='login')
def lista_jogos(request):
    jogos = Jogo.objects.all().values()
    return render(request, 'midia/lista_jogos.html', {'jogos': jogos})

@login_required(login_url='login')
def lista_filmes_series(request):
    filmes_series = FilmeSerie.objects.all().values()
    return render(request, 'midia/lista_filmes_series.html', {'filmes_series': filmes_series})

@login_required(login_url='login')
def dashboard(request):
    query = request.GET.get('q', '')
    jogos_resultado = []
    filmes_series_resultado = []

    if query:
        jogos_resultado = Jogo.objects.filter(nome__icontains=query)
        filmes_series_resultado = FilmeSerie.objects.filter(nome__icontains=query)

    resultados = list(jogos_resultado) + list(filmes_series_resultado)
    return render(request, 'midia/dashboard.html', {'resultados': resultados})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'midia/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = UsuarioCreationForm()
    return render(request, 'midia/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def listar_midias(request):
    filmes = FilmeSerie.objects.filter(categoria="Filme")
    series = FilmeSerie.objects.filter(categoria="Serie")
    return render(request, 'midia/midias.html', {'filmes': filmes, 'series': series})

def listar_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'midia/jogos.html', {'jogos': jogos})

@login_required(login_url='login')
def biblioteca(request):
    usuario = request.user
    jogos = [uj.jogo for uj in usuario.jogos_adquiridos.all()]
    filmes = [ufs.filme_serie for ufs in usuario.filmes_series_assistidos.all()]
    return render(request, 'midia/biblioteca.html', {'jogos': jogos, 'filmes': filmes})

@login_required(login_url='login')
def admin(request):
    return render(request, 'midia/midias.html')