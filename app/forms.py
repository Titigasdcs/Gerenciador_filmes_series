from django import forms
from .models import Filme, Serie

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'duracao', 'sinopse', 'site_oficial', 'data_lancamento', 'nota_avaliacao', 'genero', 'pais', 'diretor']

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['nome', 'duracao', 'sinopse', 'site_oficial', 'data_lancamento', 'nota_avaliacao', 'genero', 'pais', 'diretor']
