from django.shortcuts import render
from .models import Movie

def movie_list(request):
    genre_filter = request.GET.get('genre')
    search_query = request.GET.get('search')
    movies = Movie.objects.all()
    
    if genre_filter:
        movies = movies.filter(genres__icontains=genre_filter)
    
    if search_query:
        movies = movies.filter(title__icontains=search_query)
    
    genres = set(g for movie in Movie.objects.all() for g in movie.genres.split(','))
    
    context = {
        'movies': movies,
        'genres': genres,
        'selected_genre': genre_filter,
        'search_query': search_query,
    }
    return render(request, 'index.html', context)
