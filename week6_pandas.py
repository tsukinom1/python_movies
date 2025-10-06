import sys
import psycopg2
import pandas as pd


def main():
    # Настройки отображения для удобства чтения в консоли
    pd.set_option("display.width", 120)
    pd.set_option("display.max_columns", 20)
    pd.set_option("display.max_rows", 50)

    conn = None
    try:
        conn = psycopg2.connect(
            dbname="movies",
            user="alkuatzhumatayev",
            password="",
            host="localhost",
            port="5432",
        )

        query = (
            "SELECT id, title, year, rating, runtime, language_id, date_uploaded "
            "FROM Movies ORDER BY date_uploaded DESC NULLS LAST LIMIT 200;"
        )

        df = pd.read_sql(query, conn)

        print("\nПервые 5 строк DataFrame (head):")
        print(df.head(5))

        print("\nИнформация о DataFrame (info):")
        df.info()

        print("\nОписательная статистика (describe):")
        try:
            desc = df.describe(include='all', datetime_is_numeric=True)
        except TypeError:
            desc = df.describe(include='all')
        print(desc)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()


