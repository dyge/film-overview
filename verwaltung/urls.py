from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'verwaltung'

urlpatterns = [
    url(r"uebersicht/$", views.Uebersicht.as_view(),name='uebersicht'),
    url(r"add_film/$", views.CreateFilm.as_view(), name="newfilm"),
]
