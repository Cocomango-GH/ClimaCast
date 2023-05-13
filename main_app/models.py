from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
    location = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.location

