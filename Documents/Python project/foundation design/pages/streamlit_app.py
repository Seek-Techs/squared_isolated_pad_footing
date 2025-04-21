
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import math

# Page configuration
st.set_page_config(page_title="Square Pad Footing Design", layout="wide")

# Tabs setup
tabs = st.tabs(["Project Overview", "Punching Shear Check", "Moment & Reinforcement", "2D Plan View", "3D Reinforcement View"])

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
        # col_size = st.number_input("Column Size (mm)", value=300)
        dead_load = st.number_input("Dead Load (kN)", value=950.0)
        imposed_load = st.number_input("Imposed Load (kN)", value=200.0)
        fcu = st.number_input("Concrete Strength fcu (N/mm²)", value=35.0)
        fy = st.number_input("Steel Yield Strength fy (N/mm²)", value=500.0)
        safe_bearing = st.number_input("Safe Bearing Capacity (kN/m²)", value=170.0)

    total_load = dead_load + imposed_load
    factored_load = 1.35 * dead_load + 1.5 * imposed_load

    # Calculate initial footing size based on factored load and bearing capacity
    footing_area_calculated = 1.1 * factored_load / (1.4 * safe_bearing)  # in m²
    footing_side_calculated = np.sqrt(footing_area_calculated)  # m
    footing_side_mm_calculated = footing_side_calculated * 1000

    st.write("### Summary of Inputs")
    # st.write(f"Column size: {col_size} mm")
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
    effective_depth = footing_depth - cover_mm - (bar_diameter_mm * 0.5) # mm
    d_m = effective_depth / 1000 # m

    critical_perimeter = 2 * (column_width_mm + column_length_mm) + (4 * math.pi * effective_depth)
    Pcr = critical_perimeter

    # Area within critical perimeter (a1 + 4d)(a2 + 4d) - (4 - pi)(2d^2)
    col_width_m = column_width_mm / 1000
    col_length_m = column_length_mm / 1000
    critical_area = (col_width_m + 4 * d_m) * (col_width_m + 4 * d_m) - (4 - math.pi) * (2 * d_m)**2 
    Acr = critical_area

    column_side = col_width_m
    perimeter = 4 * (col_width_m + 2 * 1.5 * effective_depth)  # d = effective_depth assumed
    V = factored_load * 1e3  # Convert to N

    b0 = 4 * (col_width_m + effective_depth)
    v_ed = V / (b0 * effective_depth)
    v_rd_c = 0.5 * (fcu ** 0.5)

    footing_side_m = provided_footing_side_mm / 1000 # m

    # Net pressure, fnet = 1.1W/1.4Aprov
    net_upward_pressure = (1.1 * factored_load) / (1.4 * footing_side_m ** 2)
    
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

    if v_ed < v_rd_c:
        st.success("Punching shear check PASSED.")
    else:
        st.error("Punching shear check FAILED.")

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
    st.write(f"Factored moment (Mx = My): {My_kNm:.2f} kNm/m") # Corrected unit display

    # Effective depth should ideally be calculated based on footing depth, cover, and bar diameter
    # Using the value from Punching Shear for consistency, but consider a separate input or calculation if needed
    effective_depth_mm = st.number_input("Effective Depth (d) for Moment (mm)", value=effective_depth, min_value=50.0)
    fy_Nmm2 = fy # Using fy from the sidebar

    # Eurocode 2 calculation for required steel area
    fcd_Nmm2 = 0.85 * fcu / 1.5  # Design compressive strength of concrete (using fcu as fck approx.)
    K = My_kNm * 1e6 / (fcd_Nmm2 * 1000 * effective_depth_mm**2) # b = 1000 mm for per meter width

    K_bal = 0.167  # Approximate balanced K for concrete grade around C30 (EC2) - ADJUST IF NEEDED FOR YOUR fcu
    if K > K_bal:
        st.warning("Section requires compression reinforcement or increased depth based on simplified K_bal.")

    la = effective_depth_mm * (0.5 + math.sqrt(0.25 - K / 1.134))  # Lever arm (z in EC2)
    if la > 0.95 * effective_depth_mm:
        la = 0.95 * effective_depth_mm

    As_required = (My_kNm * 1e6) / (0.87 * fy_Nmm2 * la) # mm²/m (Required steel area per meter width)
    st.write(f"Required reinforcement area (Ast): {As_required:.2f} mm²/m")

    # Reinforcement Suggestion Logic with Preferred Spacings
    bar_options = [12, 16, 20]
    max_spacing = 300  # mm
    min_spacing = 50   # mm
    suitable_options = []
    preferred_spacings = [100, 125, 150, 175, 200, 225, 250, 300]

    for bar_dia in bar_options:
        area_per_bar = (math.pi * bar_dia ** 2) / 4  # mm²
        for n_bars in range(math.ceil(As_required / area_per_bar), 21): # Start with a reasonable lower bound for n_bars
            spacing = 1000 / n_bars  # mm
            Ast_provided_per_meter = n_bars * area_per_bar

            if min_spacing <= spacing <= max_spacing and Ast_provided_per_meter >= As_required * 0.95: # Allow a small under-provision
                suitable_options.append({
                    'bar_dia': bar_dia,
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

# ... (Rest of your code)
# ----------------------------
# 4. 2D Plan View Tab
# ----------------------------
with tabs[3]:
    st.header("2D Plan View")

    # Ensure column dimensions are in meters
    # col_size_m = col_size / 1000  # Assuming col_size is in mm from earlier input
    # col_width_m = col_size_m  # For a square column
    # col_length_m = col_size_m # For a square column

    provided_footing_side_m = provided_footing_side_mm / 1000 # Ensure footing side is in meters

    # Footing outline
    x_footing = [0, 0, provided_footing_side_m, provided_footing_side_m, 0]
    y_footing = [0, provided_footing_side_m, provided_footing_side_m, 0, 0]

    # Column outline centered in footing
    x_col = [
        provided_footing_side_m/2 - col_width_m/2,
        provided_footing_side_m/2 + col_width_m/2,
        provided_footing_side_m/2 + col_width_m/2,
        provided_footing_side_m/2 - col_width_m/2,
        provided_footing_side_m/2 - col_width_m/2
    ]
    y_col = [
        provided_footing_side_m/2 - col_length_m/2,
        provided_footing_side_m/2 - col_length_m/2, 
        provided_footing_side_m/2 + col_length_m/2,
        provided_footing_side_m/2 + col_length_m/2,
        provided_footing_side_m/2 - col_length_m/2
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
    provided_side_mm_3d = st.number_input("Footing Side Length for 3D View (mm)", value=int(footing_side_mm_calculated), help="Visualize reinforcement in this size.")
    reinforcement_spacing = st.number_input("Reinforcement Spacing (mm)", value=int(spacing) if 'spacing' in locals() else 150, min_value=50)
    bar_positions_x = np.arange(50, provided_side_mm_3d, reinforcement_spacing)
    bar_positions_y = np.arange(50, provided_side_mm_3d, reinforcement_spacing)
    center_3d = provided_side_mm_3d / 2
    col_half_3d = provided_side_mm_3d / 2

    fig3d = go.Figure()
    for x in bar_positions_x:
        fig3d.add_trace(go.Scatter3d(x=[x, x], y=[0, provided_side_mm_3d], z=[0, 0],
                                    mode='lines', line=dict(color='red', width=5), name='Bar X'))
    for y in bar_positions_y:
        fig3d.add_trace(go.Scatter3d(x=[0, provided_side_mm_3d], y=[y, y], z=[-10, -10],
                                    mode='lines', line=dict(color='green', width=5), name='Bar Y'))
    # Column block
    fig3d.add_trace(go.Mesh3d(
        x=[center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d, center_3d - col_half_3d,
           center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d, center_3d - col_half_3d],
        y=[center_3d - col_half_3d, center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d,
           center_3d - col_half_3d, center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d],
        z=[0, 0, 0, 0, 300, 300, 300, 300],
        color='blue', opacity=0.5, name='Column', showscale=False
    ))
    fig3d.update_layout(title="3D Reinforcement View", scene=dict(
        xaxis=dict(title='X (mm)'), yaxis=dict(title='Y (mm)'), zaxis=dict(title='Z (mm)'),
        aspectratio=dict(x=1, y=1, z=0.3)
    ))
    st.plotly_chart(fig3d, use_container_width=True)