from django.urls import path
from .views import list_movies, add_movie, add_suggest

urlpatterns = [
    path('movies/', list_movies),
    path('movies/add', add_movie),
    path('suggest/add', add_suggest)
]