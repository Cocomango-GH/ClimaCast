from django import forms
from .models import Location
#new code added 
class LocationForm(forms.ModelForm):
    city = forms.CharField(max_length=50)

    class Meta:
        model = Location
        fields = ('city',)


# class WeatherForm(forms.ModelForm):
#     class Meta:
#         model = Weather
#         fields = ['name', 'latitude', 'longitude', 'country', 'location']
