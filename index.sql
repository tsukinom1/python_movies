DROP TABLE IF EXISTS Torrents;
DROP TABLE IF EXISTS MovieGenres;
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Genres;
DROP TABLE IF EXISTS Languages;

CREATE TABLE Languages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    iso_code VARCHAR(10),
    region VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW(),
    description TEXT
);

CREATE TABLE Movies (
    id SERIAL PRIMARY KEY,
    imdb_code VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    title_long VARCHAR(255),
    slug VARCHAR(255),
    year INT,
    rating NUMERIC(2,1),
    runtime INT,
    language_id INT,
    summary TEXT,
    description_full TEXT,
    yt_trailer_code VARCHAR(20),
    background_image TEXT,
    large_cover_image TEXT,
    state VARCHAR(20),
    date_uploaded TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (language_id) REFERENCES Languages(id)
);

CREATE TABLE MovieGenres (
    movie_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(id),
    FOREIGN KEY (genre_id) REFERENCES Genres(id)
);

CREATE TABLE Torrents (
    id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    quality VARCHAR(20),
    size VARCHAR(50),
    url TEXT,
    video_codec VARCHAR(20),
    audio_channels VARCHAR(10),
    bit_depth VARCHAR(10),
    seeds INT,
    peers INT,
    date_uploaded TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

CREATE TABLE Genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    parent_genre_id INT,
    description TEXT,
    popularity_score NUMERIC(5,2),
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (parent_genre_id) REFERENCES Genres(id)
);
