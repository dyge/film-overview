from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'verwaltung'

urlpatterns = [
    url(r"uebersicht/$", views.Uebersicht.as_view(),name='uebersicht'),
    url(r"add_film/$", views.CreateFilm.as_view(), name="newfilm"),
    url(r'^film/(?P<pk>\d+)$', views.FilmDetailView.as_view(), name='film_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.FilmUpdateView.as_view(), name='film_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.FilmDeleteView.as_view(), name='film_remove'),
]
