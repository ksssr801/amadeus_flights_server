import requests
from dotenv import load_dotenv
import os
from django.core.cache import cache
from utilities import api_handlers
load_dotenv()

class AuthHandler:
    def __init__(self) -> None:
        self.api_key = os.environ.get('AMADEUS_API_KEY', '')
        self.api_secret = os.environ.get('AMADEUS_API_SECRET', '')
    
    def get_access_token(self, cache_config={}) -> str:
        """
        Obtain access token using Amadeus API key and secret.
        Returns:
            str: Access token for making API requests.
        """
        cache_key = cache_config.get('cache_key', '')
        if cache_key:
            cached_response = cache.get(cache_key)
            if cached_response:
                return cached_response        
        try:
            end_point = '/v1/security/oauth2/token'
            client_data = {
                "grant_type": "client_credentials",
                "client_id": self.api_key,
                "client_secret": self.api_secret
            }
            token_data = api_handlers.APIHandler().post_handler(
                end_point=end_point, 
                payload=client_data
            )
            token_timeout = token_data.get('expires_in', 900)
            access_token = token_data.get('access_token', '')
            if cache_key:
                cache.set(cache_key, access_token, token_timeout)
            return access_token
        except Exception as e:
            print(f'Error obtaining access token: {e}')
            return None
