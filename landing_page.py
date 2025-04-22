import streamlit as st
from PIL import Image

# --- Page configuration ---
st.set_page_config(page_title="Square Pad Footing Design", layout="wide")

# --- Load logo ---
logo_path = "logo.jpg"  # Replace with the actual path to your logo file
try:
    logo = Image.open(logo_path)
except FileNotFoundError:
    st.error(f"Logo not found at {logo_path}. Please make sure the file is in the correct location.")
    logo = None  # Set logo to None so we can still run the rest of the app

# --- Tabs setup ---
tabs = st.tabs(["Project Overview", "Punching Shear Check", "Moment & Reinforcement", "2D Plan View", "3D Reinforcement View"])

# --- 1. Project Overview Tab ---
with tabs[0]:
    # --- Structure the main content area ---
    col1, col2 = st.columns([1, 3])  # Adjust column widths as needed for layout

    # --- Logo in the top left of the main content ---
    with col1:
        if logo:  # Only show the logo if it loaded successfully
            st.image(logo, width=150)  # Adjust size as needed

    # --- Title and introduction in the main content ---
    with col2:
        st.title("Square Pad Footing Design")
        st.markdown(
            """
        <div style="text-align: justify;">
            This application performs the structural design of a square pad footing
            supporting a centrally loaded square column based on Eurocode 2 provisions.
            Enter your input parameters in the sidebar to get started.
        </div>
        """,
        unsafe_allow_html=True
        )

st.title("👷 Welcome to FootingPro")
st.subheader("A Professional Tool for Isolated Pad Footing Design")

st.markdown(
    """
**FootingPro** is a powerful web tool for engineers and students to design isolated footings with ease.
Built for accessibility, clarity, and structural accuracy.

### 🌟 Features:
- Input dead & live loads
- Use material strengths and soil capacity
- Calculate required footing area
- Get footing size recommendations
"""
)

col1, col2 = st.columns(2)

with col1:
    st.image("square-isolated-footing.webp", caption="Example footing sketch", use_container_width=True)

with col2:
    st.markdown("### 🚀 Get Started")
    st.markdown("Click the button below to start designing your pad footing!")

    if st.button("Launch Design Tool"):
        st.switch_page("pages/streamlit_app.py")
# --- Footer ---
st.markdown(
    """<br><br><br><br>
<div class="footer">
    <a href="mailto:your-email@example.com">Contact</a> |
    <a href="https://www.linkedin.com/your-linkedin-profile" target="_blank">LinkedIn</a> |
    Disclaimer |
    Version 1.0
</div>
""",
    unsafe_allow_html=True,
)



