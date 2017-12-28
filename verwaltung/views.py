from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models

class Uebersicht(TemplateView):
    template_name = "verwaltung/test.html"

class CreateFilm(LoginRequiredMixin, CreateView):
    form_class = forms.FilmForm
    model = models.Film
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)
