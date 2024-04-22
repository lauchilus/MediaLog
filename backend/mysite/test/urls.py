"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from api.views import AddMovieToUser, MovieRetrieveUpdateDestroy, SaveMovieView, UserMoviesList, UserMoviesUpdateDestroy, UserMovies
from animes.views import AddAnimeToUser, AnimeRetrieveUpdateDestroy, SaveAnimeView, UserAnimeUpdateDestroy, UserAnimes
from series.views import AddSerieToUser, SaveSerieView, SerieRetrieveUpdateDestroy, UserSerieUpdateDestroy, UserSeries

urlpatterns = [
    #movies
    path('save_movie/', SaveMovieView.as_view(), name='save-movie'),
    path('movie/<uuid:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='update-movie'),
    path('user/movie/', AddMovieToUser.as_view(), name='user-movie'),
    path('user/movie/<uuid:pk>/', UserMoviesUpdateDestroy.as_view(), name='user-movies'),
    path('movies/user/<str:user_id>', UserMoviesList.as_view(), name='user-movies-list'),
    #series
    path('save_serie/', SaveSerieView.as_view(), name='save-serie'),
    path('serie/<uuid:pk>/', SerieRetrieveUpdateDestroy.as_view(), name='update-serie'),
    path('user/serie/', AddSerieToUser.as_view(), name='user-serie'),
    path('user/serie/<uuid:pk>', UserSerieUpdateDestroy.as_view(), name='user-series'),
    path('series/user/<str:user_id>', UserSeries.as_view(), name='user-series-list'),
    #Anime
    path('save_anime/', SaveAnimeView.as_view(), name='save-anime'),
    path('anime/<uuid:pk>/', AnimeRetrieveUpdateDestroy.as_view(), name='update-anime'),
    path('user/anime/', AddAnimeToUser.as_view(), name='user-anime'),
    path('user/anime/<uuid:pk>', UserAnimeUpdateDestroy.as_view(), name='user-anime'),
    path('animes/user/<str:user_id>', UserAnimes.as_view(), name='user-animes-list')
]
