from django.db import models
from django.core.urlresolvers import reverse

class Film(models.Model):
    QUALS = (
        ('Kein Eintrag','Kein Eintrag'),
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
    )
    BEWS = (
        ('Keine','Keine'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    titel = models.CharField(max_length=150, unique=True)
    genre = models.CharField(max_length=100,choices=GENRES)
    ort = models.CharField(max_length=200)
    qual = models.CharField(max_length=100,choices=QUALS,default="Kein Eintrag")
    bew = models.CharField(max_length=100,choices=BEWS,default="Keine")
    class Meta:
        ordering = ('-titel',)
    def __str__(self):
        return self.titel
    def get_absolute_url(self):
        return reverse("verwaltung:film_detail",kwargs={'pk':self.pk})
