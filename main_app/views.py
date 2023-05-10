from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Weather, Location
import uuid
import boto3
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests


def home(request):
    weather_data = {}
    if request.method == 'POST':
        location = request.POST.get('location')
        api_key = os.environ.get('OPENWEATHER_API_KEY')
        url = f'http://api.openweathermap.org/data/3/weather?q={location}&units=metric&appid={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data['location'] = data['name']
            weather_data['description'] = data['weather'][0]['description']
            weather_data['temperature'] = data['main']['temp']
            weather_data['humidity'] = data['main']['humidity']
            weather_data['wind_speed'] = data['wind']['speed']
        else:
            weather_data['error'] = f'Error getting weather data for {location}. Please try again.'

    return render(request, 'home.html', {'weather_data': weather_data})


def about(request):
    return render(request, 'about.html')


class WeatherCreate(LoginRequiredMixin, CreateView):
    model = Weather
    fields = ['date', 'precipitation_chance', 'temperature', 'humidity', 'wind_speed']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WeatherUpdate(LoginRequiredMixin, UpdateView):
    model = Weather
    fields = ['date', 'precipitation_chance', 'temperature', 'humidity', 'wind_speed']


class WeatherDelete(LoginRequiredMixin, DeleteView):
    model = Weather
    success_url = '/weather/'

  
class WeatherDetail(LoginRequiredMixin, DetailView):
    model = Weather


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def location_create(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        Location.objects.create(user=request.user, location=location)
        return redirect('home')
    return render(request, 'location_form.html')


@login_required
def location_delete(request, pk):
    location = Location.objects.get(pk=pk)
    if request.user == location.user:
        location.delete()
    return redirect('home')


@login_required
def forecast(request):
    user_weather = Weather.objects.filter(user=request.user)
    forecasts = []
    for weather in user_weather:
        location = weather.location.city
        api_key = os.environ.get('OPENWEATHER_API_KEY')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            forecast = {}
            forecast['location'] = data['name']
            forecast['description'] = data['weather'][0]['description']
            forecast['temperature'] = data['main']['temp']
            forecast['humidity'] = data['main']['humidity']
            forecast['wind_speed'] = data['wind']['speed']
            forecasts.append(forecast)

    context = {'forecasts': forecasts}
    return render(request, 'weather/forecast.html', context)


