from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# from django.utilz import datetime
# from datetime import timedelta

# Create your models here.


class Movie(models.Model):
    title = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    genre = models.TextField()
    runtime = models.DurationField()

    def __str__(self):
        return self.title, self.runtime


class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    showtime = models.TimeField()


class Ticket(models.Model):
    name = models.TextField()
    purchased_at = models.DateTimeField()
    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} purchased at {self.purchased_at}"
