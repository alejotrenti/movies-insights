"""
Hero component - Movie Insights AI
Cinematic landing page hero with full-width background image
"""

from pathlib import Path

import streamlit as st
from utils.helpers import get_base64_image

hero_path = Path(__file__).resolve().parent.parent / "assets" / "images" / "hero"

background = get_base64_image(
    str(hero_path / "hero-background.jpg")
)

gallery_images = [
    get_base64_image(str(hero_path / "gallery1.jpg")),
    get_base64_image(str(hero_path / "gallery2.jpg")),
    get_base64_image(str(hero_path / "gallery3.jpg")),
    get_base64_image(str(hero_path / "gallery4.jpg")),
]

def hero(movie=None):
    """
    Render the hero section for the application landing page.
    Features a full-width background image with overlay and centered content.
    """
    
    hero_html = f"""<div class="hero-container" style="background-image: url('data:image/jpeg;base64,{background}'); background-size: cover; background-position: center; background-repeat: no-repeat;">
        <!-- Overlay -->
        <div class="hero-overlay"></div>
        <!-- Centered Content -->
        <div class="hero-content">
            <div class="hero-badge">
                <span class="badge-dot"></span>
                Movie Insights AI
            </div>
            <h1 class="hero-title">
                Discover Your<br>
                <span class="highlight">Next Favorite</span> Movie
            </h1>
            <p class="hero-description">
                Explore thousands of movies using Machine Learning,
                interactive analytics and intelligent recommendations
                powered by AI.
            </p>
            <div class="hero-buttons">
                <a href="#" class="hero-btn hero-btn-primary" style="text-decoration:none; color:white">
                    Search Movies
                </a>
                <a href="#" class="hero-btn hero-btn-secondary" style="text-decoration:none; color:white">
                    Explore Trending
                </a>
            </div>
        </div>
    </div>
    <!-- Gallery Row -->
    <div class="hero-gallery">
    <div class="hero-gallery-item">
        <img 
            src="data:image/jpeg;base64,{gallery_images[0]}"
            alt="Movie recommendations"
        >
        <span class="hero-gallery-label">
            Recommendations
        </span>
    </div>
    <div class="hero-gallery-item">
        <img 
            src="data:image/jpeg;base64,{gallery_images[1]}"
            alt="Movie analytics"
        >
        <span class="hero-gallery-label">
            Analytics
        </span>
    </div>
    <div class="hero-gallery-item">
        <img 
            src="data:image/jpeg;base64,{gallery_images[2]}"
            alt="Movie insights"
        >
        <span class="hero-gallery-label">
            Insights
        </span>
    </div>
    <div class="hero-gallery-item">
        <img 
            src="data:image/jpeg;base64,{gallery_images[3]}"
            alt="Movie trends"
        >
        <span class="hero-gallery-label">
            Trends
        </span>
    </div>
    </div>"""
    
    st.markdown(hero_html, unsafe_allow_html=True)