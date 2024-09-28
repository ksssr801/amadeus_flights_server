import requests
from django.core.cache import cache

cache_timeout = 60 * 10
base_url = 'https://test.api.amadeus.com/v2/'

class APIHandler:
    def __init__(self, api_token, cache_key):
        self.api_token = api_token
        self.cache_key = cache_key
        self.headers = {
            'Authorization': f'Bearer {self.api_token}'
        }
    
    def get_handler(self, end_point, params={}):
        cached_response = cache.get(self.cache_key)
        if cached_response:
            return cached_response
        try:
            url = f'{base_url}{end_point}'
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            cache.set(self.cache_key, data, cache_timeout)
            return data

        except Exception as e:
            return None        
    
    def post_handler(self, end_point, payload={}):
        cached_response = cache.get(self.cache_key)
        if cached_response:
            return cached_response
        try:
            url = f'{base_url}{end_point}'
            response = requests.get(url, data=payload, timeout=10)
            data = response.json()
            cache.set(self.cache_key, data, cache_timeout)
            return data

        except Exception as e:
            return None        
