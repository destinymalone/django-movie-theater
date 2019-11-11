from django.db import models

# from django.utilz import datetime
# from datetime import timedelta

# Create your models here.


class Movie(models.Model):
    title = models.TextField()
    rating = models.IntegerRangeField(min_value=1, max_value=5)
    genre = models.TextField()
    runtime = models.TimeField("%H%M")

    # def convert_timedelta(duration):
    #     days, seconds = duration.days, duration.seconds
    #     hours = days * 24 + seconds // 3600
    #     minutes = (seconds % 3600) // 60
    #     seconds = seconds % 60
    #     return hours, minutes, seconds

    # td = datetime.timedelta(2, 7743, 12345)
    # hours, minutes, seconds = convert_timedelta(td)

    def __str__(self):
        return self.title, self.runtime

    # def __str__two(self):
    #     return "{}h, {}m".format(hours, minutes)


class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    showtime = models.TimeField()


class Ticket(models.Model):
    name = models.TextField()
    purchased_at = models.DateTimeField()
    showing = models.ForeignKey(Showing, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} purchased at {self.purchased_at}"
