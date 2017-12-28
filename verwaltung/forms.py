from django import forms
from . import models

class FilmForm(forms.ModelForm):
    class Meta():
        model = models.Film
        fields = ('title','genre','ort','qual')
        widgets = {
            'ort':forms.TextInput(attrs={'placeholder': 'Box 1'}),
        }
        labels = {
            'qual':"Qualitaet",
        }
