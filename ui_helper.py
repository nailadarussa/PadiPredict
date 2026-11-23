import base64
import io
from pathlib import Path
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent


@st.cache_data(show_spinner=False)
def get_compiled_css() -> str:
    css_path = ROOT_DIR / "assets" / "styles" / "style.css"
    image_path = ROOT_DIR / "assets" / "images" / "rice-field-bg.jpeg"

    if not css_path.exists():
        return ""

    css = css_path.read_text(encoding="utf-8")

    if image_path.exists():
        # Perkecil resolusi & kompres ringan agar tidak membuat browser lag
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=75, optimize=True)
            image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        image_url = f"data:image/jpeg;base64,{image_base64}"
        css = css.replace("BACKGROUND_IMAGE", image_url)

    return css


def load_global_style():
    css = get_compiled_css()
    if css:
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
