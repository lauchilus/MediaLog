import os
from django.http import JsonResponse
from django.shortcuts import render
import requests
from dotenv import load_dotenv



# Create your views here.
load_dotenv()

headers = {
    "accept": "application/json",
    "Authorization": 'Bearer ' + os.getenv("TMDB_ACCESS_TOKEN")
}


def TMDBApiCallMoviesList(request):
    search_term = request.GET.get('q',"")
    page = request.GET.get('page',1)
    api_url = f"https://api.themoviedb.org/3/search/movie?query={search_term}&include_adult=false&language=en-US&page={page}"
    try:
        # Realiza la solicitud GET a la API externa
        response = requests.get(api_url,headers=headers)

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
        response = requests.get(api_url,headers=headers)

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
    page = request.GET.get('page',1)
    api_url = f"https://api.themoviedb.org/3/search/tv?query={search_term}&include_adult=false&language=en-US&page={page}"
    try:
        # Realiza la solicitud GET a la API externa
        response = requests.get(api_url,headers=headers)

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
        response = requests.get(api_url,headers=headers)

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