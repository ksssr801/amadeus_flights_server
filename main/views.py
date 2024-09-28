from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def flights_api_status(self, request):
    pass

@api_view(['GET'])
def flights_search(self, request):
    flights_search_params = request.GET
    origin_code = flights_search_params.get('origin_code', '')
    destination_code = flights_search_params.get('destination_code', '')
    departure_date = flights_search_params.get('departure_date', '')
    adults = flights_search_params.get('adults', None)
    limit = flights_search_params.get('limit', 5)
    
    
    pass