import json
import os
from django.core.cache import cache
import time
from django.http import JsonResponse
import requests
from dotenv import load_dotenv

load_dotenv()

def get_access_token():
    
    access_token = cache.get('access_token')
    expires_at = cache.get('access_token_expires_at')
 
    if(expires_at):
        if access_token and expires_at > time.time():
            return access_token

    
    info = fetch_new_access_token()
    print(info)

    if 'access_token' in info and 'expires_in' in info:
        cache.set('access_token', info['access_token'], timeout=info['expires_in'])
        cache.set('access_token_expires_at', time.time() + info['expires_in'])
        return info['access_token']
    else:
        return None
    cache.set('access_token', info.get('access_token',""), timeout=info.get('expires_in'))
    cache.set('access_token_expires_at', time.time() + info.get('expires_in'))

    return info.get('access_token')

def fetch_new_access_token():
    url = f'https://id.twitch.tv/oauth2/token?client_id={os.getenv('IGDB_API_CLIENT_ID')}&client_secret={os.getenv("IGDB__CLIENT_SECRET")}&grant_type=client_credentials'
    response = requests.post(url)
    if response.status_code == 200:
        data = response.json()
        
        info = {
            'access_token' : data.get('access_token'),
            'expires_in' : data.get('expires_in')
        }

        return info
    else:
            # Devuelve un mensaje de error si la solicitud falló
            return JsonResponse({'error': 'Failed to retrieve data from IGDB API'}, status=401)