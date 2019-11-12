from django.contrib import admin
from app import models


# Register your models here.

admin.site.register(models.Movie)
admin.site.register(models.Showing)
admin.site.register(models.Ticket)
