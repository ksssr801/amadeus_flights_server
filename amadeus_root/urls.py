from django.urls import path

# Custom Imports
from main.views import flights_api_status, flights_search

urlpatterns = [
    path('flights/ping/', flights_api_status, name='ping'),
    path('flights/search/', flights_search, name='search')
]