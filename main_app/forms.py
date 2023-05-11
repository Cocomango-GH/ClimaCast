from django import forms
from .models import Location, Weather

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city']

class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['name', 'latitude', 'longitude', 'country', 'location']
