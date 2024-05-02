import math
import os
from django.http import JsonResponse
from django.shortcuts import render
import requests
from dotenv import load_dotenv

from external_api.utils import get_access_token



# Create your views here.
load_dotenv()

headers_TMDB = {
    "accept": "application/json",
    "Authorization": 'Bearer ' + os.getenv("TMDB_ACCESS_TOKEN")
}

headers_MAL = {
    'X-MAL-CLIENT-ID' : os.getenv("MAL_CLIENT_ID")
}






def TMDBApiCallMoviesList(request):
    search_term = request.GET.get('q',"")
    page = int(request.GET.get('page', 1))
    api_url = f"https://api.themoviedb.org/3/search/movie?query={search_term}&include_adult=false&language=en-US&page={page}"
    try:
        # Realiza la solicitud GET a la API externa
        response = requests.get(api_url,headers=headers_TMDB)

        # Verifica si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Obtiene los datos de la respuesta JSON
            data = response.json()

            # Extrae los datos fuera del array que necesitas
            meta_info = {
                'page': data.get('page'),
                'total_pages': data.get('total_pages'),
                'total_results': data.get('total_results')
            }

            # Verifica si hay un campo que contiene una lista de objetos
            if 'results' in data:
                objects_list = data['results']

                # Filtra y selecciona solo ciertos campos de cada objeto en la lista
                filtered_objects = []
                for obj in objects_list:
                    filtered_obj = {
                        'id': obj.get('id'), 
                        'name': obj.get('title'),
                        'overview': obj.get('overview'),
                        'release_date': obj.get('release_date'),
                        'poster_url': f'https://image.tmdb.org/t/p/w500{obj.get('poster_path')}'
                    }
                    filtered_objects.append(filtered_obj)

                # Combinar los datos dentro y fuera del array en una respuesta JSON
                response_data = {
                    'pagination': meta_info,
                    'movies': filtered_objects
                }

                # Devuelve la respuesta JSON combinada
                return JsonResponse(response_data)

            else:
                return JsonResponse({'error': 'No objects found in API response'}, status=400)

        else:
            # Devuelve un mensaje de error si la solicitud falló
            return JsonResponse({'error': 'Failed to retrieve data from TMDB API'}, status=500)

    except requests.exceptions.RequestException as e:
        # Maneja las excepciones si ocurre algún error durante la solicitud
        return JsonResponse({'error': str(e)}, status=500)
    
def TMDBApiCallMovieDetails(request):
    movie_id = request.GET.get('q',"")
    api_url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    try:
        # Realiza la solicitud GET a la API externa
        response = requests.get(api_url,headers=headers_TMDB)

        # Verifica si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Obtiene los datos de la respuesta JSON
            data = response.json()

            # Extrae los datos fuera del array que necesitas
            movie = {
                    'id': data.get('id'), 
                    'name': data.get('original_title'),
                    'overview': data.get('overview'),
                    'release_date': data.get('release_date'),
                    'poster_url': f'https://image.tmdb.org/t/p/w500{data.get('poster_path')}'
            }
            print(movie)
            return JsonResponse(movie)

           

        else:
            # Devuelve un mensaje de error si la solicitud falló
            return JsonResponse({'error': 'Failed to retrieve data from TMDB API'}, status=500)

    except requests.exceptions.RequestException as e:
        # Maneja las excepciones si ocurre algún error durante la solicitud
        return JsonResponse({'error': str(e)}, status=500)
    

def TMDBApiCallSeriesList(request):
    search_term = request.GET.get('q',"")
    page = int(request.GET.get('page', 1))
    api_url = f"https://api.themoviedb.org/3/search/tv?query={search_term}&include_adult=false&language=en-US&page={page}"
    try:
        # Realiza la solicitud GET a la API externa
        response = requests.get(api_url,headers=headers_TMDB)

        # Verifica si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Obtiene los datos de la respuesta JSON
            data = response.json()

            # Extrae los datos fuera del array que necesitas
            meta_info = {
                'page': data.get('page'),
                'total_pages': data.get('total_pages'),
                'total_results': data.get('total_results')
            }

            # Verifica si hay un campo que contiene una lista de objetos
            if 'results' in data:
                objects_list = data['results']

                # Filtra y selecciona solo ciertos campos de cada objeto en la lista
                filtered_objects = []
                for obj in objects_list:
                    filtered_obj = {
                        'id': obj.get('id'), 
                        'name': obj.get('original_name'),
                        'overview': obj.get('overview'),
                        'release_date': obj.get('first_air_date'),
                        'poster_url': f'https://image.tmdb.org/t/p/w500{obj.get('poster_path')}'
                    }
                    filtered_objects.append(filtered_obj)

                # Combinar los datos dentro y fuera del array en una respuesta JSON
                response_data = {
                    'pagination': meta_info,
                    'movies': filtered_objects
                }

                # Devuelve la respuesta JSON combinada
                return JsonResponse(response_data)

            else:
                return JsonResponse({'error': 'No objects found in API response'}, status=400)

        else:
            # Devuelve un mensaje de error si la solicitud falló
            return JsonResponse({'error': 'Failed to retrieve data from TMDB API'}, status=500)

    except requests.exceptions.RequestException as e:
        # Maneja las excepciones si ocurre algún error durante la solicitud
        return JsonResponse({'error': str(e)}, status=500)
    
def TMDBApiCallSerieDetails(request):
    serie_id = request.GET.get('q',"")
    api_url = f"https://api.themoviedb.org/3/tv/{serie_id}?language=en-US"
    try:
        # Realiza la solicitud GET a la API externa
        response = requests.get(api_url,headers=headers_TMDB)

        # Verifica si la solicitud fue exitosa (código de respuesta 200)
        if response.status_code == 200:
            # Obtiene los datos de la respuesta JSON
            data = response.json()

            # Extrae los datos fuera del array que necesitas
            serie = {
                    'id': data.get('id'), 
                    'name': data.get('original_name'),
                    'overview': data.get('overview'),
                    'release_date': data.get('first_air_date'),
                    'poster_url': f'https://image.tmdb.org/t/p/w500{data.get('poster_path')}'
            }
            return JsonResponse(serie)

           

        else:
            # Devuelve un mensaje de error si la solicitud falló
            return JsonResponse({'error': 'Failed to retrieve data from TMDB API'}, status=500)

    except requests.exceptions.RequestException as e:
        # Maneja las excepciones si ocurre algún error durante la solicitud
        return JsonResponse({'error': str(e)}, status=500)


def IGDBApiCallGamesList(request):
    game = request.GET.get('q', '')
    page= int(request.GET.get('page', 1))
    api_url = 'https://api.igdb.com/v4/games'
    fields = f'fields name,summary,cover.image_id,release_dates.human;limit 15;offset {15 * (page -1)} ;search "{game}";'
    access_token = get_access_token()
    headers = {
        'Client-ID': os.getenv('IGDB_API_CLIENT_ID'),
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'  
    }

    try:
        api_response = requests.post(api_url, headers=headers,data=fields)

        # Procesa la respuesta de la API externa y devuelve una respuesta
        if api_response.status_code == 200:
            data = api_response.json()

            filtered_objects = []
            for obj in data:
                    filtered_obj = {
                        'id': obj.get('id'), 
                        'name': obj.get('name'),
                        'overview': obj.get('summary'),
                        'release_date': obj.get('release_dates')[0].get('human'),
                        'poster_url': f'https://images.igdb.com/igdb/image/upload/t_1080p/{obj.get('cover').get('image_id')}.jpg'
                    }
                    filtered_objects.append(filtered_obj)

            return JsonResponse(filtered_objects,safe = False)
        else:
            return JsonResponse({'error': 'Failed to fetch data from external API'}, status=api_response.status_code)
    except requests.exceptions.RequestException as e:
         return JsonResponse({'error': str(e)}, status=500)
    
def IGDBApiCallGamesDetails(request):
    game = request.GET.get('q', '')
    api_url = 'https://api.igdb.com/v4/games'
    fields = f'fields name,summary,cover.image_id,release_dates.human;where id={game};'
    access_token = get_access_token()
    headers = {
        'Client-ID': os.getenv('IGDB_API_CLIENT_ID'),
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'  
    }

    try:
        api_response = requests.post(api_url, headers=headers,data=fields)

        # Procesa la respuesta de la API externa y devuelve una respuesta
        if api_response.status_code == 200:
            data = api_response.json()
            processResponse = CallIgdbGames(data)

            return JsonResponse(processResponse,safe = False)
        else:
            return JsonResponse({'error': 'Failed to fetch data from external API'}, status=api_response.status_code)
    except requests.exceptions.RequestException as e:
         return JsonResponse({'error': str(e)}, status=500)


def CallIgdbGames(data):
    filtered_objects = []
    for obj in data:
        id = obj.get('id')
        name = obj.get('name')
        overview = obj.get('summary')
        release_date = obj.get('release_dates')[0].get('human') if obj.get('release_dates') else None
        cover_image_id = obj.get('cover').get('image_id') if obj.get('cover') else None
        poster_url = f'https://images.igdb.com/igdb/image/upload/t_1080p/{cover_image_id}.jpg' if cover_image_id else None

        filtered_obj = {
            'id': id,
            'name': name,
            'overview': overview,
            'release_date': release_date,
            'poster_url': poster_url
        }
        filtered_objects.append(filtered_obj)
    return filtered_objects



def IgdbListGames(request):
    page = int(request.GET.get('page', 1))
    api_url = 'https://api.igdb.com/v4/games'
    fields = f'fields name,summary,cover.image_id,release_dates.human;limit 15;offset {(15 * (page - 1))};sort rating_count desc;'
    access_token = get_access_token()
    headers = {
        'Client-ID': os.getenv('IGDB_API_CLIENT_ID'),
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'  
    }
    try:
        api_response = requests.post(api_url, headers=headers,data=fields)

        # Procesa la respuesta de la API externa y devuelve una respuesta
        if api_response.status_code == 200:
            data = api_response.json()
            processResponse = CallIgdbGames(data)

            return JsonResponse(processResponse,safe = False)
        else:
            return JsonResponse({'error': 'Failed to fetch data from external API'}, status=api_response.status_code)
    except requests.exceptions.RequestException as e:
         return JsonResponse({'error': str(e)}, status=500)


    
def SearchBooksList(request):
    search = request.GET.get('q','')
    offset = int(request.GET.get('offset', 1))
    url = f'https://openlibrary.org/search.json?q={search}&fields=key,title,author_name,author_key,publish_date,cover_i&limit=15&offset={15 *(offset-1)}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            page = math.ceil(data.get('numFound')/15) 
            meta_info = {
                'page' : 15 *(offset-1),
                'total_pages': page,
                'total_results': data.get('numFound')
            }
            if 'docs' in data:
                objects_list = data['docs']
                filtered_objects = []
                for obj in objects_list:
                    filtered_obj = {
                        'id': obj.get('key'), 
                        'title': obj.get('title'),
                        'author_name': obj.get('author_name')[0],
                        'author_key': obj.get('author_key')[0],
                        'poster_url': f'https://covers.openlibrary.org/b/id/{obj.get('cover_i')}-M.jpg'
                    }
                    filtered_objects.append(filtered_obj)
                response_data = {
                    'pagination': meta_info,
                    'books': filtered_objects
                }
                return JsonResponse(response_data)
            else:
                return JsonResponse({'error': 'No objects found in API response'}, status=400)
        else:
            return JsonResponse({'error': 'Failed to retrieve data from TMDB API'}, status=500)
    except requests.exceptions.RequestException as e:
         return JsonResponse({'error': str(e)}, status=500)
    

def BookDetails(request):
    search = request.GET.get('q','')
    url = f'https://openlibrary.org/works/{search}.json'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            
            obj = data
                
            book = {
                        'id': obj.get('key'), 
                        'title': obj.get('title'),
                        'author_key': obj.get('authors')[0].get('author').get('key'),
                        'description': obj.get('description'),
                        'poster_url': f'https://covers.openlibrary.org/b/id/{obj.get('covers')[0]}-M.jpg'
                    }
            return JsonResponse(book)
        else:
            return JsonResponse({'error': 'Failed to retrieve data from TMDB API'}, status=500)
    except requests.exceptions.RequestException as e:
         return JsonResponse({'error': str(e)}, status=500)
    
def SearchAnime(request):
    anime = request.GET.get('q','')
    url = f'https://api.myanimelist.net/v2/anime?q={anime}&limit=15'
    try:
        response = requests.get(url, headers=headers_MAL)
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
         return JsonResponse({'error': str(e)}, status=500)
    
def AnimeChangePage(request):
    url = request.body
    try:
        response = requests.get(url, headers=headers_MAL)
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
         return JsonResponse({'error': str(e)}, status=500)
    
def AnimeDetails(request):
    anime = request.GET.get('q','')
    url = f'https://api.myanimelist.net/v2/anime/{anime}?fields=id,title,main_picture,start_date,end_date,synopsis'
    try:
        response = requests.get(url, headers=headers_MAL)
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
         return JsonResponse({'error': str(e)}, status=500)
