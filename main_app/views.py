from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Location
import uuid
import boto3
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from django.db import models
from datetime import datetime
from .forms import LocationForm


#new code 
#path('', views.home, name='home'),
@login_required
def home(request):
    weather_data = {}
    if request.method == 'POST':
        location = request.POST.get('location')
        api_key = os.environ['API_KEY']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data['location'] = data['name']
            weather_data['description'] = data['weather'][0]['description']
            weather_data['temperature'] = data['main']['temp']
            weather_data['humidity'] = data['main']['humidity']
            weather_data['wind_speed'] = data['wind']['speed']
            print(weather_data)
            # Save the weather data to the Location model
            location = Location.objects.create(user=request.user, location=location, temperature=weather_data['temperature'], humidity=weather_data['humidity'], wind_speed=weather_data['wind_speed'], last_updated=datetime.now())
            # Redirect to the forecast page with location data in the URL
        else:
            weather_data['error'] = f'Error getting weather data for {location}. Please try again.'

    return render(request, 'home.html', {'weather_data': weather_data})






def about(request):
    return render(request, 'about.html')



@login_required
def forecast(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        user_weather = Location.objects.filter(user=request.user, location=location)

        forecasts = []
        for weather in user_weather:
            location = weather.location
            api_key = os.environ.get('API_KEY')
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                forecast = {}
                forecast['date'] = datetime.now()
                forecast['location'] = data['name']
                forecast['description'] = data['weather'][0]['description']
                forecast['temperature'] = data['main']['temp']
                forecast['humidity'] = data['main']['humidity']
                forecast['wind_speed'] = data['wind']['speed']
                # Convert temperature from Celsius to Fahrenheit
                forecast['temperature_f'] = (forecast['temperature'] * 1.8) + 32
                forecasts.append(forecast)

        context = {'forecasts': forecasts}
    return render(request, 'home.html', context)

@login_required
def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['city']
            Location.objects.create(user=request.user, location=location)
            return redirect('home')
    else:
        form = LocationForm()
    return render(request, 'location_form.html', {'form': form})



@login_required
def location_delete(request, pk):
    location = Location.objects.get(pk=pk)
    if request.user == location.user:
        location.delete()
    return redirect('home')



# @login_required
# def location_update(request, pk):
#     location = Location.objects.get(pk=pk)
#     if request.user == location.user:
#         location.update()
#     return redirect('home')

@login_required
def location_update(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        user_location = Location.objects.filter(user=request.user).first()
        if user_location:
            user_location.location = location
            user_location.last_updated = datetime.now()
            user_location.save()
        else:
            Location.objects.create(user=request.user, location=location, last_updated=datetime.now())
        return redirect('home')

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