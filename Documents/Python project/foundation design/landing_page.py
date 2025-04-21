# landing_page.py

import streamlit as st
from PIL import Image

st.set_page_config(page_title="FootingPro | Home", layout="wide")

st.title("👷 Welcome to FootingPro")
st.subheader("A Professional Tool for Isolated Pad Footing Design")

st.markdown("""
**FootingPro** is a powerful web tool for engineers and students to design isolated footings with ease.  
Built for accessibility, clarity, and structural accuracy.

### 🌟 Features:
- Input dead & live loads
- Use material strengths and soil capacity
- Calculate required footing area
- Get footing size recommendations
""")

col1, col2 = st.columns(2)

with col1:
    st.image("https://i.imgur.com/Z9KoLKl.png", caption="Example footing sketch", use_container_width=True)

with col2:
    st.markdown("### 🚀 Get Started")
    st.markdown("Click the button below to start designing your pad footing!")

    if st.button("Launch Design Tool"):
        st.switch_page("pages/streamlit_app.py")
