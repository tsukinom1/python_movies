import psycopg2
import pandas as pd

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="Movies5",
            user="postgres",
            password="Moldir",
            host="localhost",
            port="5432"
        )
        print("PostgreSQL connected")
        return conn
    except Exception as e:
        print("Error:", e)
        return None


conn = get_connection()

if conn:
    df_movies = pd.read_sql("""
        SELECT m.id, m.title, m.year, m.rating, m.runtime, m.language_id, l.name as language
        FROM Movies m
        LEFT JOIN Languages l ON m.language_id = l.id
    """, conn)
    print("\n--- Movies деректері (JOIN арқылы) ---\n", df_movies.head())

    df_genres = pd.read_sql("""
        SELECT mg.movie_id, g.name as genre
        FROM MovieGenres mg
        JOIN Genres g ON mg.genre_id = g.id
    """, conn)
    print("\n--- Genres деректері ---\n", df_genres.head())

    df_torrents = pd.read_sql("""
        SELECT t.movie_id, t.quality, t.size
        FROM Torrents t
    """, conn)
    print("\n--- Torrents деректері ---\n", df_torrents.head())

    conn.close()
    print("\nДеректер дайын")

    merged_df = df_movies.merge(df_genres, left_on="id", right_on="movie_id", how="inner")
    print("\n--- Merge: Movies + Genres ---\n", merged_df.head())

    merged_df = merged_df.merge(df_torrents, left_on="id", right_on="movie_id", how="left")
    print("\n--- Merge: + Torrents ---\n", merged_df.head())


    concat_df = pd.concat([
        merged_df[["title", "year"]],
        merged_df[["rating", "runtime"]],
        merged_df[["language", "genre", "quality", "size"]]
    ], axis=1)

    print("\n--- Біріктірілген кесте ---\n", concat_df.head())

    pivot_genre = merged_df.pivot_table(
        index="genre",
        values=["rating", "runtime"],
        aggfunc={"rating": "mean", "runtime": "mean"}
    ).fillna(0).sort_values(by="rating", ascending=False)

    print("\n--- Жанр бойынша орташа рейтинг ---")
    for genre, row in pivot_genre.iterrows():
        stars = "⭐" * int(round(row["rating"]))
        print(f"{genre}: {row['rating']:.2f} {stars}, Орташа уақыт: {row['runtime']:.1f} мин")

    pivot_year_genre = merged_df.pivot_table(
        index="year",
        columns="genre",
        values="rating",
        aggfunc="mean"
    ).fillna("-")

    print("\n--- Жыл-жанр бойынша рейтинг кестесі ---\n", pivot_year_genre)

    top_torrents = merged_df.sort_values(by="size", ascending=False).head(5)
    print("\n--- Үлкен torrent файлдар ---")
    for i, row in top_torrents.iterrows():
        print(f"{row['title']} ({row['quality']}): {row['size']} MB")
