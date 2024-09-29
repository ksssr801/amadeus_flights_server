from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utilities import api_handlers, auth
from utilities.cache_keys import CacheKeys

@api_view(['GET'])
def flights_api_status(request):
    return Response({'data': 'pong'})

@api_view(['GET'])
def flights_search(request):    
    flights_search_params = request.GET
    origin_code = flights_search_params.get('origin_code', '')
    destination_code = flights_search_params.get('destination_code', '')
    departure_date = flights_search_params.get('departure_date', '')
    adults = flights_search_params.get('adults', None)
    limit = flights_search_params.get('limit', 5)
    nocache = flights_search_params.get('nocache', 0)
    
    token = auth.AuthHandler().get_access_token(
        cache_config={
            'cache_key': CacheKeys.ACCESS_TOKEN.value
        }    
    )
    
    end_point = '/v2/shopping/flight-offers'
    params = {
            'originLocationCode': origin_code,
            'destinationLocationCode': destination_code,
            'departureDate': departure_date,
            'adults': adults,
            'max': limit
        }
    response = api_handlers.APIHandler().get_handler(
        end_point=end_point, 
        params=params,
        headers={
            'Authorization': f'Bearer {token}'
        },
        cache_config={
            'timeout': 60 * 10,
            'cache_key': f'{CacheKeys.FLIGHTS_SEARCH.value}:{end_point}:{params}',
            'nocache': nocache
        }    
    )
    
    return Response({'data': response})