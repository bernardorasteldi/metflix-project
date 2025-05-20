from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('jogos/', views.lista_jogos, name='lista_jogos'),
    path('filmes_series/', views.lista_filmes_series, name='lista_filmes_series'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('biblioteca/', views.biblioteca, name='biblioteca'),
    path('', lambda request: redirect('login'), name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('adicionar_jogo/<int:jogo_id>/', views.adicionar_jogo_biblioteca, name='adicionar_jogo'),
    path('adicionar_filme/<int:filme_id>/', views.adicionar_filme_serie_biblioteca, name='adicionar_filme'),
    path('remover_jogo/<int:jogo_id>/', views.remover_jogo_biblioteca, name='remover_jogo'),
    path('remover_filme/<int:filme_id>/', views.remover_filme_serie_biblioteca, name='remover_filme'),
    path('admin/', views.admin, name='admin'),
]
