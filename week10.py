import matplotlib.pyplot as plt
import pandas as pd  


def visualize_data():
    plt.style.use('seaborn-v0_8-darkgrid')


    genre_data = pd.DataFrame({
        'genre': ['Action', 'Comedy', 'Drama', 'Horror', 'Romance'],
        'movie_count': [50, 35, 70, 20, 40]
    })

    if not genre_data.empty:
        plt.figure(figsize=(10, 6))
        plt.bar(genre_data['genre'], genre_data['movie_count'], color='skyblue')
        plt.title("Количество фильмов по жанрам", fontsize=14)
        plt.xlabel("Жанры", fontsize=12)
        plt.ylabel("Количество фильмов", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    year_data = pd.DataFrame({
        'year': [2018, 2019, 2020, 2021, 2022],
        'avg_rating': [7.2, 7.5, 7.0, 7.8, 8.1]
    })

    if not year_data.empty:
        plt.figure(figsize=(10, 6))
        plt.plot(year_data['year'], year_data['avg_rating'], marker='o', linestyle='-', color='purple')
        plt.title("Средний рейтинг фильмов по годам", fontsize=14)
        plt.xlabel("Год", fontsize=12)
        plt.ylabel("Средний рейтинг", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.xticks(year_data['year'], rotation=45)
        plt.tight_layout()
        plt.show()


    if not genre_data.empty:
        plt.figure(figsize=(8, 8))
        plt.pie(genre_data['movie_count'], labels=genre_data['genre'], autopct="%1.1f%%", startangle=140,
                colors=plt.cm.Paired.colors)
        plt.title("Процентное соотношение фильмов по жанрам", fontsize=14)
        plt.tight_layout()
        plt.show()


    rating_data = pd.DataFrame({
        'rating': [5.1, 6.4, 7.2, 7.9, 8.3, 8.7, 6.8, 7.5, 7.0, 8.0]
    })

    if not rating_data.empty:
        plt.figure(figsize=(10, 6))
        plt.hist(rating_data['rating'], bins=10, color='orange', edgecolor='black', alpha=0.7)
        plt.title("Распределение рейтингов фильмов", fontsize=14)
        plt.xlabel("Рейтинг", fontsize=12)
        plt.ylabel("Количество фильмов", fontsize=12)
        plt.tight_layout()
        plt.show()


visualize_data()
