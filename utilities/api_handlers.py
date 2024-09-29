import requests
from django.core.cache import cache
from django.conf import settings

CACHE_TIMEOUT = settings.CACHE_TIMEOUT
BASE_URL = settings.AMADEUS_API_BASE_URL

class APIHandler:
    def get_handler(self, end_point, params={}, headers=None, cache_config={}):
        cache_key = cache_config.get('cache_key', '')
        nocache = cache_config.get('nocache', 0)
        if cache_key and not int(nocache):
            cached_response = cache.get(cache_key)
            if cached_response:
                return cached_response
        try:
            url = f'{BASE_URL}{end_point}'
            response = requests.get(url, params=params, headers=headers, timeout=10)
            data = response.json()
            if cache_key and not data.get('status'):
                cache.set(cache_key, data, cache_config.get('timeout', CACHE_TIMEOUT))
            return data

        except Exception as e:
            print (e)
            return None        
    
    def post_handler(self, end_point, payload={}, headers=None, cache_config={}):
        cache_key = cache_config.get('cache_key', '')
        nocache = cache_config.get('nocache', 0)
        if cache_key and not int(nocache):
            cached_response = cache.get(cache_key)
            if cached_response:
                return cached_response
        try:
            url = f'{BASE_URL}{end_point}'
            response = requests.post(url, data=payload, headers=headers, timeout=10)
            data = response.json()
            if cache_key:
                cache.set(cache_key, data, cache_config.get('timeout', CACHE_TIMEOUT))
            return data

        except Exception as e:
            print (e)
            return None        
