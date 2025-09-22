import requests
import json

url = "https://movie-database-api1.p.rapidapi.com/list_movies.json"

querystring = {
    "limit": "50",
    "page": "1",
    "quality": "all",
    "genre": "all",
    "minimum_rating": "0",
    "query_term": "0",
    "sort_by": "date_added",
    "order_by": "desc",
    "with_rt_ratings": "false"
}

headers = {
    "x-rapidapi-key": "64acfa5bc8msh47699c6231ab51cp1e607ejsn584b29027eba",
    "x-rapidapi-host": "movie-database-api1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Проверим, что в ответе есть ключ 'data' и 'movies'
if "data" in data and "movies" in data["data"]:
    movies = data["data"]["movies"]

    for movie in movies:
        # Печатаем фильм красиво JSON-форматом
        print(json.dumps(movie, indent=2, ensure_ascii=False))
        print("=" * 50)
else:
    print("Не удалось найти список фильмов в ответе:", data)
