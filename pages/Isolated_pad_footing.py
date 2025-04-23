
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import math
import io  # Import the io module
import datetime # Import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# --- Page configuration ---
st.set_page_config(page_title="Square Pad Footing Design", layout="wide")

# --- Define CSS styles ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

# Custom CSS for the button
st.markdown(
    """
    <style>
    #home_button {
        background-color: #4CAF50;  /* Green */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    #home_button:hover {
        background-color: #367c39; /* Darker green */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='app-header'>Welcome to the design tool page.</div>", unsafe_allow_html=True)

# Add a button to go back to the home page
if st.button("Go to Home", key="home_button", on_click=lambda: st.session_state.update({"launch_design": False})):
    st.switch_page("Home.py")

# --- Tabs setup ---
tabs = st.tabs(["Project Overview", "Punching Shear Check", "Moment & Reinforcement", "2D Plan View", "3D Reinforcement View", "Download Report"])

# ----------------------------
# 1. Project Overview Tab
# ----------------------------
with tabs[0]:
    st.title("Square Pad Footing Design")
    st.markdown("""
    This application performs the structural design of a square pad footing
    supporting a centrally loaded square column based on Eurocode 2 provisions.
    Enter your input parameters in the sidebar to get started.
    """)
    with st.sidebar:
        st.header("Input Parameters")
        dead_load = st.number_input("Dead Load (kN)", value=950.0)
        imposed_load = st.number_input("Imposed Load (kN)", value=200.0)
        fcu = st.number_input("Concrete Strength fcu (N/mm²)", value=35.0)
        fy = st.number_input("Steel Yield Strength fy (N/mm²)", value=500.0)
        safe_bearing = st.number_input("Safe Bearing Capacity (kN/m²)", value=170.0)
    total_load = dead_load + imposed_load
    factored_load = 1.35 * dead_load + 1.5 * imposed_load
    unit_of_concrete = 25  # kN/m³
    # Calculate initial footing size based on factored load and bearing capacity
    footing_area_calculated = 1.1 * factored_load / (1.4 * safe_bearing)  # in m²
    footing_side_calculated = np.sqrt(footing_area_calculated)  # m
    footing_side_mm_calculated = footing_side_calculated * 1000
    st.write("### Summary of Inputs")
    st.write(f"Total service load: {total_load:.2f} kN")
    st.write(f"Factored load: {factored_load:.2f} kN")
    st.write(f"Safe bearing capacity: {safe_bearing:.1f} kN/m²")
    st.write(f"Calculated Footing Size (approx): {footing_side_mm_calculated:.0f} mm × {footing_side_mm_calculated:.0f} mm")

# ----------------------------
# 2. Punching Shear Check Tab
# ----------------------------
with tabs[1]:
    st.header("Punching Shear Check")
    provided_footing_side_mm = st.number_input("Provided Footing Side Length (mm)", value=int(footing_side_mm_calculated), help="Use the actual side length you will provide.")
    footing_depth = st.number_input("Footing Depth (h) for Base (mm)", value=400, min_value=150)
    column_width_mm = st.number_input("Column width (mm)", value=300, min_value=225)
    column_length_mm = st.number_input("Column length (mm)", value=300, min_value=225)
    bar_diameter_mm = st.number_input("Reinforcement Bar Diameter (mm)", value=12, min_value=6)
    cover_mm = st.number_input("Enter concrete cover in mm:", value=50, min_value=20)
    effective_depth = footing_depth - cover_mm - (bar_diameter_mm * 0.5)  # mm
    d_m = effective_depth / 1000  # m
    critical_perimeter = 2 * (column_width_mm + column_length_mm) + (4 * math.pi * effective_depth)
    Pcr = critical_perimeter
    # Area within critical perimeter (a1 + 4d)(a2 + 4d) - (4 - pi)(2d^2)
    col_width_m = column_width_mm / 1000
    col_length_m = column_length_mm / 1000
    critical_area = (col_width_m + 4 * d_m) * (col_width_m + 4 * d_m) - (4 - math.pi) * (2 * d_m) ** 2
    Acr = critical_area
    # column_side = col_width_m

    # Selfweight of the pad base
    area_of_base = (provided_footing_side_mm / 1000) ** 2
    h = footing_depth / 1000
    selfweight = unit_of_concrete * area_of_base * h
    selfweight = selfweight  # kN

    # Maximum soil pressure
    max_soil_pressure = (factored_load + selfweight) / area_of_base
    perimeter = 4 * (col_width_m + 2 * 1.5 * effective_depth)  # d = effective_depth assumed
    V = factored_load * 1e3  # Convert to N
    b0 = 4 * (col_width_m + effective_depth)
    v_ed = V / (b0 * effective_depth)
    v_rd_c = 0.5 * (fcu ** 0.5)
    footing_side_m = provided_footing_side_mm / 1000  # m
    # Net pressure, fnet = W/Aprov  <-- Changed to use service load and provided area
    net_upward_pressure = total_load / (footing_side_m ** 2)
    # Load causing punching is the total load outside the critical perimeter, V = fnet(base area - area within critical perimeter) kN
    V_net_kN = net_upward_pressure * ((footing_side_m ** 2) - Acr)  # kN
    V_net_N = V_net_kN * 1e3  # Convert to N
    Vpunch = V_net_N / (Pcr * effective_depth)  # N/mm²
   
    st.write(f"Provided Footing Size: {provided_footing_side_mm:.0f} mm × {provided_footing_side_mm:.0f} mm")
    st.write(f"Effective Depth (d): {effective_depth} mm")
    st.write(f"Critical Perimeter (Pcr): {round(Pcr, 2)} mm")
    st.write(f"Area within critical perimeter (Acr): {round(Acr, 4)} m²")
    st.write(f"Punching shear stress (ved): {v_ed:.2f} N/mm²")
    st.write(f"Punching shear capacity (vrdc): {v_rd_c:.2f} N/mm²")
    st.write(f"Punching Shear Stress (Vpunch): {Vpunch:.3f} N/mm²")
    st.write(f"Selfweight of footing: {selfweight:.2f} kN")
    st.write(f"Maximum Soil Pressure: {max_soil_pressure:.2f} kN/m²")
    if v_ed < v_rd_c:
        st.success("Punching shear check PASSED.")
    else:
        st.error("Punching shear check FAILED.")
    if max_soil_pressure <= safe_bearing:
        st.success("Maximum soil pressure is within safe bearing capacity.")
    else:
        st.error("Maximum soil pressure EXCEEDS safe bearing capacity.")
# ----------------------------
# 3. Moment & Reinforcement Tab
# ----------------------------
with tabs[2]:
    st.header("Moment and Reinforcement Design")
    provided_footing_side_m = provided_footing_side_mm / 1000  # m
    overhang_m = (provided_footing_side_m - col_width_m) / 2  # m
    Mx_kNm = 0.5 * net_upward_pressure * (overhang_m ** 2)  # kNm/m (Moment per unit width)
    My_kNm = Mx_kNm  # Same due to square footing symmetry

    st.write(f"Provided Footing Size: {provided_footing_side_mm:.0f} mm × {provided_footing_side_mm:.0f} mm")
    st.write(f"Factored moment (Mx = My): {My_kNm:.2f} kNm/m")

    # Effective depth should ideally be calculated based on footing depth, cover, and bar diameter
    # Using the value from Punching Shear for consistency
    effective_depth_mm = st.number_input("Effective Depth (d) for Moment (mm)", value=effective_depth, min_value=50.0)
    fy_Nmm2 = fy
    fcd_Nmm2 = 0.85 * fcu / 1.5
    K = My_kNm * 1e6 / (fcd_Nmm2 * 1000 * effective_depth_mm ** 2)
    K_bal = 0.167
    if K > K_bal:
        st.warning("Section requires compression reinforcement or increased depth.")
    la = effective_depth_mm * (0.5 + math.sqrt(0.25 - K / 1.134))
    if la > 0.95 * effective_depth_mm:
        la = 0.95 * effective_depth_mm
    As_required = (My_kNm * 1e6) / (0.87 * fy_Nmm2 * la)
    st.write(f"Required reinforcement area (Ast): {As_required:.2f} mm²/m")

    # User selects ONE bar diameter
    available_bar_diameters = [10, 12, 16, 20, 25, 32]  # Add more as needed
    selected_bar_diameter = st.selectbox("Select Bar Diameter (mm)", available_bar_diameters) # corrected line
    max_spacing = 300  # mm
    min_spacing = 50  # mm
    preferred_spacings = [100, 125, 150, 175, 200, 225, 250, 300]

    area_per_bar = (math.pi * selected_bar_diameter ** 2) / 4  # mm²

    suitable_options = [] #important
    for n_bars in range(math.ceil(As_required / area_per_bar), 21):  # Iterate through a reasonable range of bar numbers
        spacing = 1000 / n_bars
        Ast_provided_per_meter = n_bars * area_per_bar
        if min_spacing <= spacing <= max_spacing and Ast_provided_per_meter >= 0.95 * As_required:
            suitable_options.append({
                'bar_dia': selected_bar_diameter,
                'area_per_bar': round(area_per_bar, 2),
                'no_bars': n_bars,
                'Ast_provided_per_meter': round(Ast_provided_per_meter, 2),
                'spacing': round(spacing, 2)
            })

    if suitable_options:
        def get_spacing_preference_score(option):
            min_diff = float('inf')
            for sp in preferred_spacings:
                diff = abs(option['spacing'] - sp)
                if diff < min_diff:
                    min_diff = diff
            return min_diff

        best_option = min(suitable_options, key=lambda x: (get_spacing_preference_score(x), abs(x['Ast_provided_per_meter'] - As_required)))

        st.subheader("Reinforcement Suggestion:")
        st.write(f"Bar Diameter: T{best_option['bar_dia']} mm")
        st.write(f"Spacing: {best_option['spacing']} mm c/c")
        st.write(f"Provided Ast: {best_option['Ast_provided_per_meter']} mm²/m")
        st.write(f"Provide T{best_option['bar_dia']} mm bars @ {best_option['spacing']} mm c/c in both directions")
        reinforcement_spacing = best_option['spacing']
        bar_diameter_for_view = best_option['bar_dia']
    else:
        st.warning("No suitable reinforcement option found within spacing limits with sufficient steel area.")
        st.write(f"Required Ast per meter: {As_required:.2f} mm²")

# ----------------------------
# 4. 2D Plan View Tab
# ----------------------------
with tabs[3]:
    st.header("2D Plan View")
    provided_footing_side_m = provided_footing_side_mm / 1000  # Ensure footing side is in meters
    # Footing outline
    x_footing = [0, 0, provided_footing_side_m, provided_footing_side_m, 0]
    y_footing = [0, provided_footing_side_m, provided_footing_side_m, 0, 0]
    # Column outline centered in footing
    x_col = [
        provided_footing_side_m / 2 - col_width_m / 2,
        provided_footing_side_m / 2 + col_width_m / 2,
        provided_footing_side_m / 2 + col_width_m / 2,
        provided_footing_side_m / 2 - col_width_m / 2,
        provided_footing_side_m / 2 - col_width_m / 2
    ]
    y_col = [
        provided_footing_side_m / 2 - col_length_m / 2,
        provided_footing_side_m / 2 - col_length_m / 2,
        provided_footing_side_m / 2 + col_length_m / 2,
        provided_footing_side_m / 2 + col_length_m / 2,
        provided_footing_side_m / 2 - col_length_m / 2
    ]
    # Create plot
    fig_plan = go.Figure()
    fig_plan.add_trace(go.Scatter(x=x_footing, y=y_footing, name='FOOTING', mode='lines', line=dict(color='red', width=1.5)))
    fig_plan.add_trace(go.Scatter(x=x_col, y=y_col, name='COLUMN', mode='lines', line=dict(color='green', width=1.5)))
    fig_plan.update_layout(
        title_text='FOOTING PLAN',
        width=500,
        height=500,
        xaxis=dict(title=f'{provided_footing_side_m:.2f} (m)', scaleanchor='y', scaleratio=1),
        yaxis=dict(title=f'{provided_footing_side_m:.2f} (m)'),
        showlegend=True
    )
    st.plotly_chart(fig_plan)

# ----------------------------
# 5. 3D Reinforcement View Tab
# ----------------------------
with tabs[4]:
    st.header("3D Reinforcement View")
    # Use the provided footing side and bar spacing for the 3D view
    provided_side_mm_3d = st.number_input("Footing Side Length for 3D View (mm)",
                                         value=int(footing_side_mm_calculated),
                                         help="Visualize reinforcement in this size.")
    reinforcement_spacing = st.number_input("Reinforcement Spacing (mm)",
                                         value=int(reinforcement_spacing) if 'reinforcement_spacing' in locals() else 150,
                                         min_value=50)
    bar_positions_x = np.arange(0, provided_side_mm_3d + reinforcement_spacing, reinforcement_spacing)  # Ensure 0 and end are included
    bar_positions_y = np.arange(0, provided_side_mm_3d + reinforcement_spacing, reinforcement_spacing)
    center_3d = provided_side_mm_3d / 2
    col_half_3d = column_width_mm / 2  # Use column_width_mm
    fig3d = go.Figure()
    # X-direction bars (running along Y-axis)
    for x in bar_positions_x:
        fig3d.add_trace(go.Scatter3d(
            x=[x, x],
            y=[0, provided_side_mm_3d],
            z=[0, 0],
            mode='lines',
            line=dict(color='red', width=3),  # Reduced width for clarity
            name='X-Bars'  # Added name for legend
        ))
    # Y-direction bars (running along X-axis)
    for y in bar_positions_y:
        fig3d.add_trace(go.Scatter3d(
            x=[0, provided_side_mm_3d],
            y=[y, y],
            z=[0, 0],
            mode='lines',
            line=dict(color='green', width=3),
            name='Y-Bars'
        ))
    # Column block - corrected and simplified
    fig3d.add_trace(go.Mesh3d(
        x=[center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d, center_3d - col_half_3d,
           center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d, center_3d - col_half_3d],
        y=[center_3d - col_half_3d, center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d,
           center_3d - col_half_3d, center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d],
        z=[0, 0, 0, 0, footing_depth, footing_depth, footing_depth, footing_depth],
        color='blue',
        opacity=0.5,
        name='Column',
        showscale=False  # Remove color scale
    ))
    fig3d.update_layout(
        title="3D Reinforcement View",
        scene=dict(
            xaxis=dict(title=f'{provided_side_mm_3d} (mm)', range=[0, provided_side_mm_3d]),  # Added range for better view
            yaxis=dict(title=f'{provided_side_mm_3d} (mm)', range=[0, provided_side_mm_3d]),
            zaxis=dict(title=f'{footing_depth} (mm)', range=[0, footing_depth]),  # Added range for Z
            aspectratio=dict(x=1, y=1, z=0.3),
            camera=dict(
                eye=dict(x=1.2, y=1.2, z=0.8)  # Adjust camera position for better view
            )
        ),
        showlegend=True  # Show legend to distinguish X and Y bars
    )
    st.plotly_chart(fig3d, use_container_width=True)
# # --- Add a download button for the report ---
# report_filename = "footing_design_report.txt"  # Name of the report file

# # Create the report content as a string
# report_content = f"""
# Square Pad Footing Design Report

# 1. Project Overview
# --------------------
# Total service load: {total_load:.2f} kN
# Factored load: {factored_load:.2f} kN
# Safe bearing capacity: {safe_bearing:.1f} kN/m²
# Calculated Footing Size (approx): {footing_side_mm_calculated:.0f} mm × {footing_side_mm_calculated:.0f} mm

# 2. Punching Shear Check
# ----------------------
# Provided Footing Size: {provided_footing_side_mm:.0f} mm × {provided_footing_side_mm:.0f} mm
# Effective Depth (d): {effective_depth} mm
# Critical Perimeter (Pcr): {Pcr:.2f} mm
# Area within critical perimeter (Acr): {Acr:.4f} m²
# Punching shear stress (ved): {v_ed:.2f} N/mm²
# Punching shear capacity (vrdc): {v_rd_c:.2f} N/mm²
# Punching Shear Stress (Vpunch): {Vpunch:.3f} N/mm²
# Punching shear check: {'PASSED' if v_ed < v_rd_c else 'FAILED'}

# 3. Moment and Reinforcement Design
# -----------------------------------
# Provided Footing Size: {provided_footing_side_mm:.0f} mm × {provided_footing_side_mm:.0f} mm
# Factored moment (Mx = My): {My_kNm:.2f} kNm/m
# Required reinforcement area (Ast): {As_required:.2f} mm²/m

# Reinforcement Suggestion:
# Bar Diameter: {best_option['bar_dia']} mm
# Spacing: {best_option['spacing']} mm c/c
# Provided Ast: {best_option['Ast_provided_per_meter']} mm²/m
# Provide T{best_option['bar_dia']} mm bars @ {best_option['spacing']} mm c/c in both directions
# """

# # Create a BytesIO object to hold the report content
# report_buffer = io.BytesIO(report_content.encode())

# # Add a download button
# st.download_button(
#     label="Download Design Report",
#     data=report_buffer,
#     file_name=report_filename,
#     mime="text/plain",  # Set the MIME type for a plain text file
#     help="Download a text file containing the design report.",
# )

# ----------------------------
# 6. Download Report Tab
# ----------------------------
with tabs[5]:
    st.header("Download Report")
    st.write("Generate a PDF report of the footing design calculations.")

    if st.button("Generate Report"):
        # Create a BytesIO buffer to hold the PDF data
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        Story = []

        # Title and Metadata
        title_style = styles['Title']
        title_style.alignment = 1  # Center
        Story.append(Paragraph("Square Pad Footing Design Report", title_style))
        Story.append(Spacer(1, 0.2 * inch))
        date_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Story.append(Paragraph(f"Date: {date_str}", styles['Normal']))
        Story.append(Spacer(1, 0.2 * inch))

        # 1. Project Overview
        Story.append(Paragraph("1. Project Overview", styles['h1']))
        Story.append(Spacer(1, 0.1 * inch))
        data = [
            ["Parameter", "Value"],
            ["Total service load (kN)", f"{total_load:.2f}"],
            ["Factored load (kN)", f"{factored_load:.2f}"],
            ["Safe bearing capacity (kN/m²)", f"{safe_bearing:.1f}"],
            ["Provided Footing Size (mm)", f"{provided_footing_side_mm:.0f} x {provided_footing_side_mm:.0f}"],
        ]
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (1, 0), 12),
            ('BACKGROUND', (0, 1), (1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        Story.append(table)
        Story.append(Spacer(1, 0.2 * inch))

        # 2. Punching Shear Check
        Story.append(Paragraph("2. Punching Shear Check", styles['h1']))
        Story.append(Spacer(1, 0.1 * inch))

        # Calculate check results beforehand
        punching_shear_check = "PASSED" if v_ed < v_rd_c else "FAILED"
        safe_bearing_check = max_soil_pressure <= safe_bearing  # Assuming max_soil_pressure is defined

        data = [
            ["Parameter", "Value"],
            ["Effective Depth (d) (mm)", f"{effective_depth}"],
            ["Critical Perimeter (Pcr) (mm)", f"{Pcr:.2f}"],
            ["Area within critical perimeter (Acr) (m²)", f"{Acr:.4f}"],
            ["Punching shear stress (ved) (N/mm²)", f"{v_ed:.2f}"],
            ["Punching shear capacity (vrdc) (N/mm²)", f"{v_rd_c:.2f}"],
            ["Punching Shear Stress (Vpunch) (N/mm²)", f"{Vpunch:.3f}"],
            ["Punching Shear Check", punching_shear_check],
            ["Safe Bearing Check", "PASSED" if safe_bearing_check else "FAILED"],  #added safe bearing check
        ]

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (1, 0), 12),
            ('BACKGROUND', (0, 1), (1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('TEXTCOLOR', (1, 7), (1, 7), colors.green if v_ed < v_rd_c else colors.red), # Changed index to 7
            ('TEXTCOLOR', (1, 8), (1, 8), colors.green if safe_bearing_check else colors.red),  # Added color for safe bearing check
        ]))
        Story.append(table)
        Story.append(Spacer(1, 0.2 * inch))

        # 3. Moment & Reinforcement Design
        Story.append(Paragraph("3. Moment & Reinforcement Design", styles['h1']))
        Story.append(Spacer(1, 0.1 * inch))
        data = [
            ["Parameter", "Value"],
            ["Factored moment (Mx = My) (kNm/m)", f"{My_kNm:.2f}"],
            ["Required reinforcement area (Ast) (mm²/m)", f"{As_required:.2f}"]
        ]
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (1, 0), 12),
            ('BACKGROUND', (0, 1), (1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        Story.append(table)
        Story.append(Spacer(1, 0.1 * inch))

        if 'best_option' in locals():
            Story.append(Paragraph("Reinforcement Suggestion:", styles['h2']))
            data = [
                ["Parameter", "Value"],
                ["Bar Diameter (mm)", f"T{best_option['bar_dia']}"],
                ["Spacing (mm c/c)", f"{best_option['spacing']}"],
                ["Provided Ast (mm²/m)", f"{best_option['Ast_provided_per_meter']}"]
            ]
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (1, 0), colors.lightgrey),
                ('TEXTCOLOR', (0, 0), (1, 0), colors.black),
                ('ALIGN', (0, 0), (1, 0),'CENTER'),
                ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (1, 0), 12),
                ('BACKGROUND', (0, 1), (1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            Story.append(table)
        else:
            Story.append(Paragraph("No suitable reinforcement option found.", styles['Normal']))
        Story.append(Spacer(1, 0.2 * inch))

        Story.append(Paragraph("4. 2D Plan View: (See application for plot)", styles['h1']))
        Story.append(Spacer(1, 0.2 * inch))
        Story.append(Paragraph("5. 3D Reinforcement View: (See application for 3D plot)", styles['h1']))

        doc.build(Story)
        buffer.seek(0)

        # Download button
        st.download_button(
            label="Download PDF Report",
            data=buffer,
            file_name="footing_design_report.pdf",
            mime="application/pdf",
            help="Download a PDF report of the footing design calculations.",
        )
