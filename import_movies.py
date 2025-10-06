import json
import psycopg2

conn = psycopg2.connect(
    dbname="movies",
    user="alkuatzhumatayev",
    password="",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

with open("movies.json", encoding="utf-8") as f:
    movies_data = json.load(f)

languages_cache = {}
genres_cache = {}

for movie in movies_data:
    lang_name = movie.get("language", "Unknown")
    if lang_name not in languages_cache:
        cur.execute("INSERT INTO Languages (name) VALUES (%s) ON CONFLICT (name) DO NOTHING RETURNING id;", (lang_name,))
        lang_id = cur.fetchone()
        if lang_id is None:
            cur.execute("SELECT id FROM Languages WHERE name=%s;", (lang_name,))
            lang_id = cur.fetchone()
        languages_cache[lang_name] = lang_id[0]
    language_id = languages_cache[lang_name]

    cur.execute("""
        INSERT INTO movies (imdb_code, title, title_long, slug, year, rating, runtime, language_id,
                            summary, description_full, yt_trailer_code, background_image, large_cover_image,
                            state, date_uploaded)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (imdb_code) DO NOTHING RETURNING id;
    """, (
        movie.get("imdb_code"),
        movie.get("title"),
        movie.get("title_long"),
        movie.get("slug"),
        movie.get("year"),
        movie.get("rating"),
        movie.get("runtime"),
        language_id,
        movie.get("summary"),
        movie.get("description_full"),
        movie.get("yt_trailer_code"),
        movie.get("background_image"),
        movie.get("large_cover_image"),
        movie.get("state"),
        movie.get("date_uploaded")
    ))
    movie_id = cur.fetchone()
    if movie_id is None:
        cur.execute("SELECT id FROM Movies WHERE imdb_code=%s;", (movie.get("imdb_code"),))
        movie_id = cur.fetchone()
    movie_id = movie_id[0]

    for genre_name in movie.get("genres", []):
        if genre_name not in genres_cache:
            cur.execute("INSERT INTO Genres (name) VALUES (%s) ON CONFLICT (name) DO NOTHING RETURNING id;", (genre_name,))
            genre_id = cur.fetchone()
            if genre_id is None:
                cur.execute("SELECT id FROM Genres WHERE name=%s;", (genre_name,))
                genre_id = cur.fetchone()
            genres_cache[genre_name] = genre_id[0]
        genre_id = genres_cache[genre_name]

        cur.execute("""
            INSERT INTO MovieGenres (movie_id, genre_id)
            VALUES (%s, %s)
            ON CONFLICT (movie_id, genre_id) DO NOTHING;
        """, (movie_id, genre_id))

    for torrent in movie.get("torrents", []):
        cur.execute("""
            INSERT INTO Torrents (movie_id, quality, size, url, video_codec, audio_channels, bit_depth, seeds, peers, date_uploaded)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, (
            movie_id,
            torrent.get("quality"),
            torrent.get("size"),
            torrent.get("url"),
            torrent.get("video_codec"),
            torrent.get("audio_channels"),
            torrent.get("bit_depth"),
            torrent.get("seeds"),
            torrent.get("peers"),
            torrent.get("date_uploaded")
        ))

conn.commit()
cur.close()
conn.close()
print("Данные успешно загружены!")
