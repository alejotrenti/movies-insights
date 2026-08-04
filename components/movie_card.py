import streamlit as st
from utils.posters import get_poster

def movie_card(movie):

    """
    Render a movie card.

    Parameters
    ----------
    movie : pandas Series or dict
        Movie information.
    """

    title = movie.get("title", "Unknown")

    rating = movie.get(
        "vote_average",
        "N/A"
    )

    release_date = movie.get(
        "release_date",
        "Unknown"
    )

    overview = movie.get(
        "overview",
        ""
    )


    # Poster placeholder por ahora
    poster = (
        movie.get("poster_path")
        if movie.get("poster_path")
        else "https://via.placeholder.com/300x450"
    )

    poster = get_poster(movie["id"])
    
    st.markdown(
        f"""<div class="movie-card">
                <img 
                    class="movie-poster"
                    src="{poster}"
                >
            <div class="movie-info">
                <h3 class="movie-title">
                    {title}
                </h3>
                <div class="movie-meta">
                    <span class="movie-rating">
                        ⭐ {rating}
                    </span>
                    <span>
                        {str(release_date)[:4]}
                    </span>
                </div>
                <p class="movie-description">
                    {overview[:120]}...
                </p>
            </div>
        </div>""",
        unsafe_allow_html=True
    )
