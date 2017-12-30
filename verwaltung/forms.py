from django import forms
from . import models

class FilmForm(forms.ModelForm):
    class Meta():
        model = models.Film
        fields = ('titel','genre','ort','qual','bew')
        widgets = {
            'ort':forms.TextInput(attrs={'placeholder': 'Box 1'}),
        }
        labels = {
            'qual':"Qualitaet",
            'bew':"Bewertung",
        }
