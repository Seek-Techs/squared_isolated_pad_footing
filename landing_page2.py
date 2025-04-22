import streamlit as st
from PIL import Image

# --- Page configuration ---
st.set_page_config(page_title="FootingCalc Pro", layout="wide")  # Consistent title

# --- Load logo ---
logo_path = "logo.jpg"  # Replace with the actual path to your logo file
logo_width = 200  # Adjust as needed
try:
    logo = Image.open(logo_path)
except FileNotFoundError:
    st.error(f"Logo not found at {logo_path}. Please make sure the file is in the correct location.")
    logo = None  # Set logo to None so we can still run the rest of the app

# --- Main landing page content ---
def main_page():
    # --- Header Section ---
    header_col1, header_col2 = st.columns([1, 2])  # Adjust column widths for logo and title
    with header_col1:
        if logo:
            st.image(logo, width=logo_width)  # Display logo
    with header_col2:
        st.title("FootingCalc Pro")
        st.markdown("Design Civil Footings with Confidence")

    st.markdown("<br><br>", unsafe_allow_html=True)  # Add vertical spacing

    # --- Start Designing Button ---
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <button style="
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 10px;
            ">Start Designing</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Use st.session_state to control page switch
    if st.session_state.get("launch_design", False):
        st.switch_page("pages/streamlit_app.py")

    # Create a button.  Set the key.  Use session state to switch
    if st.button("Start Designing", key="start_design_button", on_click=lambda: st.session_state.update({"launch_design": True})):
        pass

    st.markdown("<br><br>", unsafe_allow_html=True)  # Add vertical spacing

    # --- App Name and Overview Text ---
    st.markdown(
        """
        **FootingCalc Pro**
        This app allows you to design isolated pad footings based on
        safe bearing capacity, load values, and material strengths—
        all in one click.
        """
    )

    st.markdown("<br><br>", unsafe_allow_html=True)  # Add vertical spacing

    # --- Benefit Panels ---
    st.subheader("Key Benefits")
    benefit_col1, benefit_col2, benefit_col3, benefit_col4 = st.columns(4)
    with benefit_col1:
        st.markdown("### Easy Design")
        st.image("logo.jpg", width=100)  # Replace with actual image
    with benefit_col2:
        st.markdown("### Auto-Report")
        st.image("logo.jpg", width=100)  # Replace with actual image
    with benefit_col3:
        st.markdown("### Visual Diagrams")
        st.image("logo.jpg", width=100)  # Replace with actual image
    with benefit_col4:
        st.markdown("### Educational")
        st.image("logo.jpg", width=100)  # Replace with actual image

    st.markdown("<br><br><br>", unsafe_allow_html=True)  # Add vertical spacing

    # --- Footer ---
    st.markdown(
        """
        <div style="text-align: center; color: gray;">
            Contact | LinkedIn | Disclaimer | Version
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Tabs setup ---  (moved to the main app file)
tabs = st.tabs(["Project Overview", "Punching Shear Check", "Moment & Reinforcement", "2D Plan View", "3D Reinforcement View"])

# --- 1. Project Overview Tab --- (moved to the main app file)
with tabs[0]:
#     # --- Structure the main content area ---
    col1, col2 = st.columns([1, 3])  # Adjust column widths as needed for layout
#
#     # --- Logo in the top left of the main content ---
    with col1:
        if logo:  # Only show the logo if it loaded successfully
            st.image(logo, width=150)  # Adjust size as needed
#
#     # --- Title and introduction in the main content ---
    with col2:
        st.title("Square Pad Footing Design")
        st.markdown(
            """
            This application performs the structural design of a square pad footing
            supporting a centrally loaded square column based on Eurocode 2 provisions.

            Enter your input parameters in the sidebar to get started.
            """
        )

# --- Run the main page ---
if "launch_design" not in st.session_state:
    st.session_state["launch_design"] = False
main_page()
