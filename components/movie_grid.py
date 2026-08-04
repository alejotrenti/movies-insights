import streamlit as st

from components.movie_card import movie_card


def movie_grid(movies, columns=4):
    """
    Render a grid of movie cards.s

    Parameters
    ----------
    movies : pandas DataFrame
        DataFrame containing movie information.

    columns : int
        Number of cards per row.
    """

    if movies.empty:
        st.warning("No movies found.")
        return


    cols = st.columns(columns)


    for index, (_, movie) in enumerate(movies.iterrows()):

        column = cols[index % columns]

        with column:
            movie_card(movie)