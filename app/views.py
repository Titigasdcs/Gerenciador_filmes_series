from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import (Filme, FilmeAtor, Genero, Serie, SerieEpisodio, Temporada, Ator, Diretor, Pais, Continente, Episodio)
from .models import Filme
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Filme, Serie
from .forms import FilmeForm, SerieForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        total_filmes = Filme.objects.count()
        total_series = Serie.objects.count()
        total_atores = Ator.objects.count()
        total_paises = Pais.objects.count()
        filmes = Filme.objects.all()[:5]

        return render(request, 'index.html', {
            'filmes': filmes,
            'total_filmes': total_filmes,
            'total_series': total_series,
            'total_atores': total_atores,
            'total_paises': total_paises,
        })

class FilmeView(View):
    def get(self, request, *args, **kwargs):
        filmes = Filme.objects.select_related('genero', 'pais', 'diretor').all()
        return render(request, 'filmes.html', {'filmes': filmes})


class FilmeCreateView(View):
    def get(self, request):
        return render(request, 'filme_form.html')

    def post(self, request):
        nome = request.POST['nome']
        Filme.objects.create(nome=nome, duracao=120, sinopse="...", nota_avaliacao=5)
        return redirect('filmes')


class FilmeEditView(View):
    def get(self, request, pk):
        filme = get_object_or_404(Filme, pk=pk)
        return render(request, 'filme_form.html', {'filme': filme})

    def post(self, request, pk):
        filme = get_object_or_404(Filme, pk=pk)
        filme.nome = request.POST['nome']
        filme.save()
        return redirect('filmes')


class FilmeDeleteView(View):
    def get(self, request, pk):
        filme = get_object_or_404(Filme, pk=pk)
        filme.delete()
        return redirect('filmes')
    
class GeneroView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'generos.html', {'generos': generos})

class FilmeAtorView(View):
    def get(self, request, *args, **kwargs):
        filme_atores = FilmeAtor.objects.select_related('filme', 'ator').all()
        return render(request, 'filmes_atores.html', {'filme_atores': filme_atores})

class SerieView(View):
    def get(self, request, *args, **kwargs):
        series = Serie.objects.all()
        return render(request, 'series.html', {'series': series})


class SerieEpisodioView(View):
    def get(self, request, *args, **kwargs):
        serie_episodios = SerieEpisodio.objects.select_related(
            'serie', 'temporada', 'episodio'
        ).all()
        return render(request, 'serie_episodios.html', {'serie_episodios': serie_episodios})



class EpisodioView(View):
    def get(self, request, *args, **kwargs):
        episodios = Episodio.objects.all()
        return render(request, 'episodios.html', {'episodios': episodios})



class TemporadaView(View):
    def get(self, request, *args, **kwargs):
        temporadas = Temporada.objects.all()
        return render(request, 'temporadas.html', {'temporadas': temporadas})

class AtorView(View):
    def get(self, request, *args, **kwargs):
        atores = Ator.objects.all()
        return render(request, 'atores.html', {'atores': atores})


class DiretorView(View):
    def get(self, request, *args, **kwargs):
        diretores = Diretor.objects.all()
        return render(request, 'diretores.html', {'diretores': diretores})

class PaisView(View):
    def get(self, request, *args, **kwargs):
        paises = Pais.objects.select_related('continente').all()
        return render(request, 'paises.html', {'paises': paises})


class ContinenteView(View):
    def get(self, request, *args, **kwargs):
        continentes = Continente.objects.all()
        return render(request, 'continentes.html', {'continentes': continentes})

class FilmeCreateView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'criar_filme.html'
    success_url = reverse_lazy('filmes')

class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'editar_filme.html'
    success_url = reverse_lazy('filmes')

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'excluir_filme.html'
    success_url = reverse_lazy('filmes')

class SerieCreateView(CreateView):
    model = Serie
    form_class = SerieForm
    template_name = 'criar_serie.html'
    success_url = reverse_lazy('series')

class SerieUpdateView(UpdateView):
    model = Serie
    form_class = SerieForm
    template_name = 'editar_serie.html'
    success_url = reverse_lazy('series')

class SerieDeleteView(DeleteView):
    model = Serie
    template_name = 'excluir_serie.html'
    success_url = reverse_lazy('series')

 