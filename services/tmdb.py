import pandas as pd
import ast


MOVIES_PATH = "data/movies.csv"
CREDITS_PATH = "data/credits.csv"


# Cargar datasets
movies_df = pd.read_csv(MOVIES_PATH)
credits_df = pd.read_csv(CREDITS_PATH)


# Unimos ambos datasets
movies = movies_df.merge(
    credits_df,
    left_on="id",
    right_on="movie_id",
    how="left"
)


# Limpieza básica
movies["title"] = movies["title_x"]


def get_trending(limit=10):
    """
    Películas ordenadas por popularidad
    """
    return movies.sort_values(
        by="popularity",
        ascending=False
    ).head(limit)



def search_movie(query, limit=10):
    """
    Buscar películas por título
    """
    results = movies[
        movies["title"]
        .str.contains(
            query,
            case=False,
            na=False
        )
    ]

    return results.head(limit)



def get_movie_details(movie_id):
    """
    Obtener detalles de una película
    """

    movie = movies[
        movies["id"] == movie_id
    ]

    if movie.empty:
        return None

    return movie.iloc[0]