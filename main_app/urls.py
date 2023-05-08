from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('climacast/', include('climacast.urls')),
    path('admin/', admin.site.urls),
]