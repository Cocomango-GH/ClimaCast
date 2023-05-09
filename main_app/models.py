from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.city


class Weather(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
