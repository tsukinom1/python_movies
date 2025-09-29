import psycopg2
import numpy as np

conn = psycopg2.connect(
    dbname="Movies5",
    user="postgres",
    password="Moldir",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Загружаем данные: id, title, year, rating, runtime
cur.execute("""
    SELECT id, title, year, rating, runtime 
    FROM Movies
""")
movies = cur.fetchall()

# Преобразуем в массив NumPy
movies_np = np.array(movies, dtype=object)

# 1. 10 фильмов с самыми высокими рейтингами
top_rated_indices = np.argsort(movies_np[:,3].astype(float))[::-1][:10]
top_rated = movies_np[top_rated_indices]
print("10 фильмов с самыми высокими рейтингами:")
for movie in top_rated:
    print(f"{movie[1]} ({movie[2]}), рейтинг: {movie[3]}, длительность: {movie[4]} мин")

# 2. Средняя длительность фильмов по годам
years = np.unique(movies_np[:,2])
print("\nСредняя длительность фильмов по годам:")
for year in years:
    runtimes = movies_np[movies_np[:,2] == year][:,4].astype(float)
    if len(runtimes) > 0:
        print(f"{year}: {np.mean(runtimes):.2f} мин")

# 3. Количество фильмов по годам (динамика)
print("\nКоличество фильмов по годам:")
for year in years:
    count = np.sum(movies_np[:,2] == year)
    print(f"{year}: {count} фильмов")

cur.close()
conn.close()
