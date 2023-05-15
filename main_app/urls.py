from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('climacast', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('location/create/', views.location_create, name='location_create'),
    path('location/<int:pk>/delete/', views.location_delete, name='location_delete'),
    path('forecast/', views.forecast, name='forecast'),
]
