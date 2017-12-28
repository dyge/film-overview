from django.db import models

class Film(models.Model):
    QUALS = (
        ('sehr gut','Sehr gut'),
        ('gut','Gut'),
        ('mittel','Mittel'),
        ('schlecht','Schlecht'),
    )
    GENRES = (
        ('comedy','Komoedie'),
        ('horror','Horror'),
    )
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100,choices=GENRES)
    ort = models.CharField(max_length=200)
    qual = models.CharField(max_length=100,choices=QUALS)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("home")
