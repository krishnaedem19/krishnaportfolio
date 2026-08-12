import base64
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Edem Krishna Chaithanya | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def image_to_data_uri(path: Path) -> str:
    mime = "image/jpeg" if path.suffix.lower() in [".jpg", ".jpeg"] else "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"

html = load_text(BASE_DIR / "templates" / "index.html")
css = load_text(BASE_DIR / "static" / "style.css")
js = load_text(BASE_DIR / "static" / "script.js")
profile_uri = image_to_data_uri(BASE_DIR / "assets" / "profile.jpg")

html = html.replace("{{PROFILE_IMAGE}}", profile_uri)
html = html.replace("{{CSS}}", css)
html = html.replace("{{JS}}", js)

# Hide Streamlit's default chrome so the portfolio feels like a standalone website.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        [data-testid="stAppViewContainer"] > .main {padding-top: 0;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.components.v1.html(html, height=3300, scrolling=True)

# Native Streamlit download control for the resume.
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
with open(BASE_DIR / "assets" / "resume.pdf", "rb") as f:
    st.download_button(
        "Download Resume PDF",
        data=f,
        file_name="Edem_Krishna_Chaithanya_Resume.pdf",
        mime="application/pdf",
        use_container_width=False,
    )
