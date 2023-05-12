from django.urls import path
from . import views
from .views import home, forecast


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('weather/create/', views.WeatherCreate.as_view(), name='weather_create'),
    # path('weather/<int:pk>/', views.WeatherDetail.as_view(), name='weather_detail'),
    # path('weather/<int:pk>/update/', views.WeatherUpdate.as_view(), name='weather_update'),
    # path('weather/<int:pk>/delete/', views.WeatherDelete.as_view(), name='weather_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('location/create/', views.location_create, name='location_create'),
    path('location/<int:pk>/delete/', views.location_delete, name='location_delete'),
    # path('location/<int:pk>/edit/', views.location_edit, name='location_edit'),
    path('location/<int:pk>/delete/', views.location_delete, name='location_delete'),
    path('forecast/', views.forecast, name='forecast'),
    path('climacast/', views.home, name='climacast'),
    path('forecast/', forecast, name='forecast'),
    

]

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('accounts/signup/', views.signup, name='signup'),
#     path('location/create/', views.location_create, name='location_create'),
#     path('location/<int:pk>/delete/', views.location_delete, name='location_delete'),
#     path('forecast/', views.forecast, name='forecast'),
#     path('climacast/', views.home, name='climacast'),
# ]
