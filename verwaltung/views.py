from django.views.generic import TemplateView, CreateView,DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from django.urls import reverse_lazy

class Uebersicht(TemplateView):
    template_name = "verwaltung/test.html"

class CreateFilm(LoginRequiredMixin, CreateView):
    form_class = forms.FilmForm
    model = models.Film
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class FilmDetailView(DetailView):
    model = models.Film

class FilmUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'verwaltung/film_detail.html'
    form_class = forms.FilmForm
    model = models.Film

class FilmDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Film
    success_url = reverse_lazy('home')
