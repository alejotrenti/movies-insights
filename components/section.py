import streamlit as st


def section(title: str, subtitle: str | None = None):
    """
    Render a section header.
    """

    html = f"""<div class="section">
        <h2 class="section-title">
            {title}
        </h2>"""

    if subtitle:
        html += f"""<p class="section-subtitle">
            {subtitle}
        </p>"""

    html += "</div>"

    st.markdown(
        html,
        unsafe_allow_html=True
    )