from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Continente(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Pais(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    continente = models.ForeignKey(
        Continente, on_delete=models.SET_NULL, null=True, related_name="paises"
    )

    def __str__(self):
        return f"{self.nome} ({self.continente})" if self.continente else self.nome


class Diretor(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=100)
    site = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Ator(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=100)
    site = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    nome = models.CharField(max_length=200)
    duracao = models.PositiveIntegerField(help_text="Duração em minutos")
    sinopse = models.TextField()
    site_oficial = models.URLField(blank=True, null=True)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    genero = models.ForeignKey(
        Genero, on_delete=models.SET_NULL, null=True, related_name="filmes"
    )
    pais = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, related_name="filmes"
    )
    diretor = models.ForeignKey(
        Diretor, on_delete=models.SET_NULL, null=True, related_name="filmes"
    )

    def __str__(self):
        return self.nome


class FilmeAtor(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name="atores")
    ator = models.ForeignKey(Ator, on_delete=models.CASCADE, related_name="filmes")

    def __str__(self):
        return f"{self.ator.nome} em {self.filme.nome}"


class Serie(models.Model):
    nome = models.CharField(max_length=200)
    duracao = models.PositiveIntegerField(help_text="Duração média dos episódios (min)")
    sinopse = models.TextField()
    site_oficial = models.URLField(blank=True, null=True)
    data_lancamento = models.DateField()
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    genero = models.ForeignKey(
        Genero, on_delete=models.SET_NULL, null=True, related_name="series"
    )
    pais = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, related_name="series"
    )
    diretor = models.ForeignKey(
        Diretor, on_delete=models.SET_NULL, null=True, related_name="series"
    )

    def __str__(self):
        return self.nome


class Temporada(models.Model):
    serie = models.ForeignKey("Serie", on_delete=models.CASCADE, null=True, blank=True)
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.serie.nome} - Temporada {self.numero}" if self.serie else f"Temporada {self.numero}"



class Episodio(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class SerieEpisodio(models.Model):
    serie = models.ForeignKey(
        Serie, on_delete=models.CASCADE, related_name="episodios",
        null=True, blank=True  # <-- adicionado
    )
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    episodio = models.ForeignKey(Episodio, on_delete=models.CASCADE)
    duracao = models.IntegerField()
    data_disponibilizacao = models.DateField()

