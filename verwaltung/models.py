from django.db import models
from django.core.urlresolvers import reverse

class Film(models.Model):
    QUALS = (
        ('sehr gut','sehr gut'),
        ('gut','gut'),
        ('mittel','mittel'),
        ('schlecht','schlecht'),
    )
    GENRES = (
        ('Comedy','Comedy'),
        ('Horror','Horror'),
        ('Action','Action'),
        ('Fantasy','Fantasy'),
        ('Drama','Drama'),
        ('Adventure','Adventure'),
        ('Sci-fi','Sci-fi'),
        ('Animation','Animation'),
        ('Crime','Crime'),
        ('Mystery','Mystery'),
        ('Romance','Romance'),
        ('Romance','Romance'),
    )
    title = models.CharField(max_length=150, unique=True)
    genre = models.CharField(max_length=100,choices=GENRES)
    ort = models.CharField(max_length=200)
    qual = models.CharField(max_length=100,choices=QUALS)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("home",kwargs={'pk':self.pk})
