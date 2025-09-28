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

if "data" in data and "movies" in data["data"]:
    movies = data["data"]["movies"]

    for i, movie in enumerate(movies, 1):
        print("=" * 100)
        print(f"Фильм №{i}")
        print("=" * 100)
        print(f"ID: {movie.get('id')}")
        print(f"Название: {movie.get('title')}")
        print(f"Полное название: {movie.get('title_long')}")
        print(f"Год выпуска: {movie.get('year')}")
        print(f"Рейтинг: {movie.get('rating')}")
        print(f"Длительность: {movie.get('runtime')} минут")
        print(f"Жанры: {', '.join(movie.get('genres', []))}")
        print(f"Язык: {movie.get('language')}")
        print(f"IMDB: https://www.imdb.com/title/{movie.get('imdb_code')}")
        print(f"Ссылка на трейлер: https://www.youtube.com/watch?v={movie.get('yt_trailer_code')}")
        print(f"Краткое описание: {movie.get('summary')}")
        print(f"Полное описание: {movie.get('description_full')}")
        print(f"Фон: {movie.get('background_image')}")
        print(f"Постер: {movie.get('large_cover_image')}")


        if "torrents" in movie:
            print("\n📥 Торренты:")
            for torrent in movie["torrents"]:
                print(f"  - Качество: {torrent.get('quality')}, Размер: {torrent.get('size')}, "
                      f"Ссылка: {torrent.get('url')}")

        print("\n")

else:
    print("Не удалось найти список фильмов в ответе:", data)

