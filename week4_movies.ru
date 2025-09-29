import psycopg2
import numpy as np
from datetime import datetime

conn = psycopg2.connect(
    dbname="Movies5",
    user="postgres",
    password="Moldir",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    SELECT runtime, rating, year, language_id, date_uploaded
    FROM Movies
    LIMIT 50;
""")
rows = cur.fetchall()

cur.close()
conn.close()

runtime_list = [row[0] for row in rows]
rating_list = [row[1] for row in rows]
year_list = [row[2] for row in rows]
language_id_list = [row[3] for row in rows]
date_uploaded_list = [row[4] for row in rows]

print("Runtime:", runtime_list)
print("Rating:", rating_list)
print("Year:", year_list)
print("Language IDs:", language_id_list)
print("Date uploaded:", date_uploaded_list)

runtime_array = np.array(runtime_list, dtype=np.float64)
rating_array = np.array(rating_list, dtype=np.float64)
year_array = np.array(year_list, dtype=np.float64)
language_id_array = np.array(language_id_list, dtype=np.int64)

# Конвертируем даты в datetime для вычислений
date_uploaded_array = np.array([datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S') if d else None for d in date_uploaded_list])

print("\nСредняя длительность фильмов:", np.mean(runtime_array))
print("Максимальный рейтинг фильмов:", np.max(rating_array))
print("Минимальный год выпуска:", np.min(year_array))
print("Уникальные ID языков:", np.unique(language_id_array))
print("Последняя дата загрузки фильма:", max([d for d in date_uploaded_array if d is not None]))
