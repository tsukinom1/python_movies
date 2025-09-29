import json

with open("movies.json", "r", encoding="utf-8") as f:
    movies_data = json.load(f)

movies_list = []

for movie in movies_data:
    movie_dict = {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "year": movie.get("year"),
        "rating": movie.get("rating"),
        "runtime": movie.get("runtime"),
        "language": movie.get("language"),
        "genres": movie.get("genres"),
        "imdb": f"https://www.imdb.com/title/{movie.get('imdb_code')}",
        "trailer": f"https://www.youtube.com/watch?v={movie.get('yt_trailer_code')}"
    }
    movies_list.append(movie_dict)

print("Первые 5 фильмов:")
for m in movies_list[:5]:
    print(m["title"], "-", m["year"], "-", m["rating"])

high_rating = [m for m in movies_list if m["rating"] >= 7]
print("\nФильмы с рейтингом >= 7:")
for m in high_rating:
    print(m["title"], "-", m["rating"])

horror_movies = [m for m in movies_list if "Horror" in m["genres"]]
print("\nФильмы жанра Horror:")
for m in horror_movies:
    print(m["title"], "-", m["genres"])

sorted_by_year = sorted(movies_list, key=lambda x: x["year"], reverse=True)
print("\n5 самых новых фильмов:")
for m in sorted_by_year[:5]:
    print(m["title"], "-", m["year"])
