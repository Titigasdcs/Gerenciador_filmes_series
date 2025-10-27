from django.contrib import admin
from .models import (Filme, FilmeAtor, Genero, Serie, Episodio, SerieEpisodio,Temporada, Ator, Diretor, Pais, Continente)


class FilmeAtorInline(admin.TabularInline):
    model = FilmeAtor
    extra = 1


class SerieEpisodioInline(admin.TabularInline):
    model = SerieEpisodio
    extra = 1


class TemporadaInline(admin.TabularInline):
    model = Temporada
    extra = 1


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Continente)
class ContinenteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("nome", "continente")
    list_filter = ("continente",)
    search_fields = ("nome",)


@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ("nome", "nacionalidade", "instagram", "site")
    search_fields = ("nome", "nacionalidade")
    list_filter = ("nacionalidade",)


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ("nome", "nacionalidade", "instagram", "site")
    search_fields = ("nome", "nacionalidade")
    list_filter = ("nacionalidade",)


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_lancamento", "nota_avaliacao", "genero", "diretor")
    list_filter = ("genero", "pais", "diretor")
    search_fields = ("nome", "sinopse")
    inlines = [FilmeAtorInline]
    ordering = ("-data_lancamento",)


@admin.register(FilmeAtor)
class FilmeAtorAdmin(admin.ModelAdmin):
    list_display = ("filme", "ator")
    list_filter = ("filme", "ator")
    search_fields = ("filme__nome", "ator__nome")


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_lancamento", "nota_avaliacao", "genero", "diretor")
    list_filter = ("genero", "pais", "diretor")
    search_fields = ("nome", "sinopse")
    inlines = [TemporadaInline]
    ordering = ("-data_lancamento",)


@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    list_display = ("serie", "numero")
    list_filter = ("serie",)
    search_fields = ("serie__nome",)
    inlines = [SerieEpisodioInline]
    ordering = ("serie", "numero")


@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(SerieEpisodio)
class SerieEpisodioAdmin(admin.ModelAdmin):
    list_display = ("temporada", "episodio", "duracao", "data_disponibilizacao")
    list_filter = ("temporada__serie",)
    search_fields = ("episodio__nome", "temporada__serie__nome")
    ordering = ("temporada", "episodio")
