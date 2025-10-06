import string
import psycopg2
import numpy as np
from datetime import datetime

conn = psycopg2.connect(
    dbname="movies",
    user="alkuatzhumatayev",
    password="",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


cur.execute(
    """
    SELECT id, title, year, rating, runtime, language_id, date_uploaded
    FROM Movies
    WHERE title ILIKE 'The Glenarma Tapes'
    ORDER BY rating DESC NULLS LAST, year DESC NULLS LAST
    LIMIT 1;
    """,
)
row = cur.fetchone()

cur.close()
conn.close()

if not row:
    print("Фильм не найден.")
else:
    movie_id, title, year, rating, runtime, language_id, date_uploaded = row
    print("\n" + "=" * 60)
    print("НАЙДЕН ФИЛЬМ")
    print("=" * 60)
    print(f"ID:            {movie_id}")
    print(f"Название:      {title}")
    print(f"Год:           {year if year is not None else '—'}")
    print(f"Рейтинг:       {float(rating):.1f}" if rating is not None else "Рейтинг:       —")
    print(f"Длительность:  {runtime} мин" if runtime is not None else "Длительность:  —")
    print(f"Язык (ID):     {language_id if language_id is not None else '—'}")
    print(f"Загружен:      {date_uploaded.strftime('%Y-%m-%d %H:%M:%S') if isinstance(date_uploaded, datetime) else (str(date_uploaded) if date_uploaded else '—')}")
    print("=" * 60)



# runtime_list = [row[0] for row in rows]
# rating_list = [row[1] for row in rows]
# year_list = [row[2] for row in rows]
# language_id_list = [row[3] for row in rows]
# date_uploaded_list = [row[4] for row in rows]

# print("Runtime:", runtime_list)
# print("=" * 50)
# print("Rating:", rating_list)
# print("=" * 50)
# print("Year:", year_list)
# print("=" * 50)
# print("Language IDs:", language_id_list)
# print("=" * 50)
# print("Date uploaded:", date_uploaded_list)
# print("=" * 50)

# runtime_array = np.array(runtime_list, dtype=np.float64)
# rating_array = np.array(rating_list, dtype=np.float64)
# year_array = np.array(year_list, dtype=np.int16)
# language_id_array = np.array(language_id_list, dtype=np.int64)


# # date_uploaded_array = np.array([datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S') if d else None for d in date_uploaded_list])

# print("\nСредняя длительность фильмов:", np.mean(runtime_array))
# print("Максимальный рейтинг фильмов:", np.max(rating_array))
# print("Минимальный год выпуска:", np.min(year_array))
# print("Уникальные ID языков:", np.unique(language_id_array))
# print("Последняя дата загрузки фильма:", max([d for d in date_uploaded_array if d is not None]))
