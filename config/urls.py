from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView, FilmeView, FilmeCreateView, FilmeEditView, FilmeDeleteView,
    SerieView, AtorView, DiretorView, GeneroView,
    PaisView, ContinenteView, TemporadaView, FilmeAtorView, SerieEpisodioView,FilmeUpdateView, SerieView, SerieCreateView, SerieUpdateView, SerieDeleteView, EpisodioView

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    # Filmes CRUD
    path('filmes/', FilmeView.as_view(), name='filmes'),
    path('filmes/novo/', FilmeCreateView.as_view(), name='filme_create'),
    path('filmes/editar/<int:pk>/', FilmeEditView.as_view(), name='filme_edit'),
    path('filmes/excluir/<int:pk>/', FilmeDeleteView.as_view(), name='filme_delete'),

    # Outros
    path('series/', SerieView.as_view(), name='series'),
    path('atores/', AtorView.as_view(), name='atores'),
    path('diretores/', DiretorView.as_view(), name='diretores'),
    path('generos/', GeneroView.as_view(), name='generos'),
    path('paises/', PaisView.as_view(), name='paises'),
    path('continentes/', ContinenteView.as_view(), name='continentes'),
    path('temporadas/', TemporadaView.as_view(), name='temporadas'),
    path('filmes-atores/', FilmeAtorView.as_view(), name='filmes_atores'),
    path('episodios/', EpisodioView.as_view(), name='episodios'),
    path('serie-episodios/', SerieEpisodioView.as_view(), name='serie_episodios'),
    path('filmes/<int:pk>/editar/', FilmeUpdateView.as_view(), name='editar_filme'),
    path('filmes/<int:pk>/excluir/', FilmeDeleteView.as_view(), name='excluir_filme'),


    
    path('series/<int:pk>/editar/', SerieUpdateView.as_view(), name='serie_update'),
    path('series/<int:pk>/deletar/', SerieDeleteView.as_view(), name='serie_delete'),


]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

