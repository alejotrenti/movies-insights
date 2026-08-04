import streamlit as st

from utils.helpers import load_css

from services.tmdb import get_trending

from components.hero import hero
from components.section import section
from components.movie_grid import movie_grid


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Movie Insights AI",
    page_icon="🎬",
    layout="wide"
)


# -----------------------------
# Load CSS
# -----------------------------
load_css("assets/css/main.css")
load_css("assets/css/cards.css")
load_css("assets/css/hero.css")


# -----------------------------
# Data
# -----------------------------
trending_movies = get_trending(10)

featured_movie = trending_movies.iloc[0]


# -----------------------------
# Hero
# -----------------------------
hero(featured_movie)


# -----------------------------
# Trending
# -----------------------------
section(
    title="🔥 Trending Movies",
    subtitle="The most popular movies right now."
)

movie_grid(trending_movies)