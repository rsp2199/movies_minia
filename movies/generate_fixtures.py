import json

movies = []

for i in range(1, 101):
    movie = {
        "model": "movies.movie",
        "pk": i,
        "fields": {
            "title": f"Movie Title {i}",
            "poster": f"https://example.com/poster{i}.jpg",
            "genres": "Action, Drama",
            "rating": "PG-13",
            "year_release": 2000 + i % 20,
            "metacritic_rating": 50 + i % 50,
            "runtime": 90 + i % 30
        }
    }
    movies.append(movie)

with open('movies/fixtures/movies.json', 'w') as f:
    json.dump(movies, f, indent=4)
