import base64
import streamlit as st


def load_css(path: str) -> None:
    """
    Load a CSS file into the Streamlit app.
    """
    with open(path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def get_base64_image(path: str) -> str:
    """
    Convert an image into a Base64 string so it can be
    embedded directly into HTML/CSS.

    Parameters
    ----------
    path : str
        Path to the image.

    Returns
    -------
    str
        Base64 encoded image.
    """
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")