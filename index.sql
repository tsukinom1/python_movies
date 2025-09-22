CREATE TABLE movies (
    id              BIGINT PRIMARY KEY,         -- id из API
    url             TEXT,                       -- ссылка на фильм
    title           TEXT NOT NULL,              -- короткое название
    title_long      TEXT NOT NULL ,                       -- полное название
    slug            TEXT NOT NULL ,                       -- slug (уникальное имя)
    year            INT NOT NULL ,                        -- год выпуска
    rating          NUMERIC(3,1),               -- рейтинг (например 5.0)
    runtime         INT NOT NULL ,                        -- длительность (в минутах)
    genres          TEXT[] NOT NULL,                     -- массив жанров
    description_full TEXT,                      -- описание
    yt_trailer_code TEXT,                       -- код трейлера на YouTube
    language        VARCHAR(10),                -- язык (например "en")
    background_image TEXT,                      -- ссылка на картинку
    date_uploaded   TIMESTAMP                   -- дата загрузки
);
